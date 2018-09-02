from django.db import models
from django.utils import timezone


class Card(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='menu name')
    description = models.CharField(max_length=128, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

# class CardItem(models.Model):
#