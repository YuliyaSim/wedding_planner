from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
]


class Wedding(models.Model):
    wedding_name = models.CharField(max_length=100)
    wedding_date = models.DateField(default=date.today)
    wedding_time = models.TimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner1_gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="", editable=False)
    partner1_email = models.EmailField(max_length=70,blank=True, null=True, unique=True)
    partner2_gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="", editable=False)
    partner2_email = models.EmailField(max_length=70,blank=True, null=True, unique=True)


    def __str__(self):
        return f'{self.wedding_name} {self.user}'


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True, null=True)
    message = models.CharField(max_length=1000)