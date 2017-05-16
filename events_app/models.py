from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Event(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=True, max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(blank=True, max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    deposit_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    @property
    def balance(self):
        return self.total_price - self.deposit_paid

    # def nothing_paid(self):
    #     return self.deposit_paid == 0

    day_contact = models.CharField(blank=True, max_length=100)
    other_info = models.TextField(null=True)

    def __str__(self):
        return self.name
