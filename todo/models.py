from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown when called


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called


class Coordinator(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True)
    website = models.URLField(max_length=250)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    notes = models.CharField(max_length=1000)

    def __str__(self):
        return self.name



class WeddingDay(models.Model):
    time = models.CharField(max_length=250, blank=True, null=True)
    item = models.CharField(max_length=500)
    notes = models.TextField(u'Notes', help_text=u'Notes', blank=True, null=True)

    def __str__(self):
        return (f'{self.time} {self.item} {self.notes}')
