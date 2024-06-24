from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserLogin(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class CustomUserRegister(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'age', 'gender']

