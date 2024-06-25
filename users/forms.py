from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Product


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserLogin(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class CustomUserRegister(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'age', 'gender')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'info', 'price')

