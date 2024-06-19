from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('MARKETING', 'Marketing'),
        ('SALES', 'Sales'),
        ('CUSTOMER', 'Customer')
    ]

    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='MALE'
    )
    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES,
        default='CUSTOMER'
    )

