from django.db import models
from django.contrib.auth.models import AbstractUser


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

    age = models.PositiveIntegerField(null=False, blank=True, default=0, db_default=0)
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

