from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from cloudstorage.settings import MEDIA_ROOT
from .forms import *
from .models import *
from .utils import *

import os
def redirect_home(request):
    return redirect("home")

def about(request):
    return render(request, 'cloud/about.html', {'menu': menu, 'title': 'About'})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'],title = request.FILES['docfile'].name ,owner = request.user.username)
            newdoc.save()

            return HttpResponseRedirect("")
    else:
        form = DocumentForm()

    documents = Document.objects.filter(owner = request.user.username)

    return render(request, 'cloud/index.html', {'documents': documents, 'form': form})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not Found 404 :(</h1>')

@csrf_exempt
def delete_files(request, id=None):

    if request.method == 'POST':
        for key in request.POST.keys():
            if 'document' in key:
                try:
                    print(MEDIA_ROOT + key)
                    os.remove(os.path.join(MEDIA_ROOT, key))
                except:
                    pass
                Document.objects.filter(docfile=key, owner=request.user.username).delete()
    return HttpResponseRedirect("/home")

def download_documents(request):

    if request.method == 'POST':
        for key in request.POST.keys():
            if 'document' in key:
                response = download(request, key)
    return response

def download(request, path):
    file_path = os.path.join(MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
   
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cloud/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cloud/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return '/home'


def logout_user(request):
    logout(request)
    return redirect('login')