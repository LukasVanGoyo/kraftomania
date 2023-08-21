
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomUser
from django.contrib import messages
from django.contrib.auth import get_user_model, password_validation
from django.core import validators
from django.contrib import messages
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    error_messages = {
            'password_mismatch':'Wpisane hasła nie są identyczne!',
        }
     
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'id': 'floatingInput','class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
    email = forms.CharField(label='Adres Email', widget=forms.TextInput(attrs={'id': 'floatingEmail','class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'id': 'floatingPassword','class': 'form-control', 'placeholder': 'Hasło'}))
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput(attrs={'id': 'floatingPasswordConfirmation','class': 'form-control', 'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


    
        