from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter(name='department_access')
def department_access(user, department_name):
    department_name = department_name.split(',')
    return user.is_superuser or user.groups.filter(name__in=department_name).exists()