from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): #structure
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form): #creation structure
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
