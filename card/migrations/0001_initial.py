# Generated by Django 2.1 on 2018-09-04 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True, verbose_name='Menu name.')),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the item on the menu.', max_length=48)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preparation_time', models.IntegerField(help_text='Time in minutes.')),
                ('classification', models.CharField(choices=[('normal', 'Normal'), ('vegetarian', 'Vegetarian')], default=0, help_text='Select if this item classifies as Vegetarian or Neither.', max_length=10, verbose_name='classification')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('card', models.ManyToManyField(to='card.Card')),
            ],
        ),
    ]
