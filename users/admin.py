from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import NewUserCreationForm, NewUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "age", "gender", "department"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "gender", "department")}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "gender", "department")}),)


admin.site.register(CustomUser, CustomUserAdmin)

