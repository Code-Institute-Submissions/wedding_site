from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Event(models.Model):

    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    date_time = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

