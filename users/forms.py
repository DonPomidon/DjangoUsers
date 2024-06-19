from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')


class NewUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('age', 'gender', 'department')

