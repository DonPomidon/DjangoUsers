from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import NewUserCreationForm, NewUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = CustomUser
    list_display = ['name', 'email', 'age', 'gender', 'department']


admin.site.register(CustomUser, CustomUserAdmin)

