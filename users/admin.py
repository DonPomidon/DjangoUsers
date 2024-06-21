from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "gender",
        "department"
    ]
    fieldsets = [
        ('Login info: ', {"fields": ("username", "email")}),
        ('Additional info', {"fields": ("age", "gender", "department")}),
    ]
    add_fieldsets = [
        ('Login info: ', {"fields": ("username", "password1", "password2", "email")}),
        ('Additional info', {"fields": ("age", "gender", "department")}),
    ]


admin.site.register(CustomUser, CustomUserAdmin)

