from __future__ import unicode_literals
from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=70)
    invited_by = models.CharField(max_length=250, null=True, blank=True)
    save_the_date = models.CharField(max_length=250, null=True, blank=True)
    invitation = models.CharField(max_length=250, null=True, blank=True)
    response = models.CharField(max_length=250, null=True, blank=True)
    attending = models.CharField(max_length=250, null=True, blank=True)
    children = models.CharField(max_length=250, null=True, blank=True)
    dietary_restrictions = models.CharField(max_length=500, null=True, blank=True)
    table_number = models.CharField(max_length=250, null=True, blank=True)
    gift_description = models.CharField(max_length=250, null=True, blank=True)
    thank_you_sent = models.CharField(max_length=250, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return 'Guest: {} {}'.format(self.first_name, self.last_name)
