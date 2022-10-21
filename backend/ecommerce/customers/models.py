from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomerManager

class Customer(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    
    CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]
    gender = models.CharField(max_length=6,choices = CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone','gender']

    objects = CustomerManager()

    def __str__(self):
        return self.email