# Generated by Django 4.2 on 2023-04-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimage', models.ImageField(upload_to='carimages')),
                ('car_name', models.CharField(blank=True, max_length=250, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=250, null=True)),
                ('customer_username', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('booking_from', models.DateTimeField(blank=True, null=True)),
                ('booking_to', models.DateTimeField(blank=True, null=True)),
                ('confirm_at', models.DateTimeField(blank=True, null=True)),
                ('booking_status', models.BooleanField(default=False)),
                ('journey_status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'car_booking',
            },
        ),
        migrations.CreateModel(
            name='car_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimage', models.ImageField(upload_to='carimages')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('seats', models.IntegerField()),
                ('fuel', models.CharField(blank=True, max_length=100, null=True)),
                ('mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('luggage', models.CharField(blank=True, max_length=250, null=True)),
                ('descripton', models.CharField(blank=True, max_length=250, null=True)),
                ('features', models.CharField(blank=True, max_length=250, null=True)),
                ('addedat', models.DateTimeField(auto_now_add=True)),
                ('rent_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'car_details',
            },
        ),
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('createdat', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'subscriber',
            },
        ),
    ]
