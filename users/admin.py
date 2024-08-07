from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Product


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
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    ]
    add_fieldsets = [
        ('Login info: ', {"fields": ("username", "password1", "password2", "email")}),
        ('Additional info', {"fields": ("age", "gender", "department")}),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
