# Generated by Django 4.0.10 on 2024-03-31 13:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(default='street', max_length=255)),
                ('city', models.CharField(default='city', max_length=200)),
                ('state_province', models.CharField(default='state', max_length=200)),
                ('postal_code', models.CharField(default='postal_code', max_length=50)),
                ('country', models.CharField(default='country', max_length=200)),
                ('firstname', models.CharField(default='firstname', max_length=255)),
                ('lastname', models.CharField(max_length=200)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_user.admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
