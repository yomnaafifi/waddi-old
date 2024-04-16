# Generated by Django 4.0.10 on 2024-03-31 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=200)),
                ('card_number', models.CharField(max_length=50)),
                ('expiration_date', models.DateField()),
                ('cvv_code', models.CharField(max_length=50)),
                ('billing_address', models.CharField(max_length=255)),
                ('card_type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('default_card', models.BooleanField()),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='driver.driver')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
