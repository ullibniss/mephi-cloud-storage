from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from captcha.fields import CaptchaField
from .models import *



class DocumentForm(forms.Form):

    def __init__(self,*args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['docfile'].widget.attrs.update({'class':'form-control'})

    docfile = forms.FileField(
        label='Select a file',
    )
    

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))