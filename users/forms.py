from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserRegister


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class CustomUserLogin(forms.Form):
    username = forms.CharField(
        label="Ведіть ваше ім\'я та прізвище:",
        max_length=100,
        required=True,
        strip=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        localize=True,
        validators=[],
        initial='DenKudrev',
    )
    password = forms.CharField(
        label="Ведіть ваш пароль:",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        localize=True,
        validators=[],
        error_messages={},
    )


class CustomUserRegister(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password', 'age', 'gender']

