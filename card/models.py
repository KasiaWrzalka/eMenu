from django.db import models
from django.utils import timezone
from rest_framework import serializers


class Card(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='Menu name.')
    description = models.CharField(max_length=128, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.name

    def number_of_items(self):
        return self.carditem_set.all().count()


class CardItem(models.Model):
    CLASSIFICATION_CHOICES = (
        ('normal', 'Normal'),
        ('vegetarian', 'Vegetarian'),
    )

    card = models.ManyToManyField(Card)
    name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
    description = models.CharField(max_length=128, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.IntegerField(help_text='Time in minutes.')
    classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES, default=0,
                                      verbose_name='classification',
                                      help_text='Select if this item classifies as Vegetarian or Neither.')
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.name

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'created_date', 'updated_date', 'number_of_items')
