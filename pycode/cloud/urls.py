
from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', redirect_home),
    path('home/', upload_file, name='home'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path(r'^delete_document/$', delete_files, name='delete'),
    path(r'^download_document/$', download_documents, name='download')
]