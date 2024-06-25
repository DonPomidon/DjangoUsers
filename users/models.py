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

    age = models.PositiveIntegerField(blank=False, db_default=0)
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
    email = models.EmailField(unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
