# Generated by Django 5.0.3 on 2024-03-19 00:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(default='firstname', max_length=255),
        ),
    ]