# Generated by Django 5.0.3 on 2024-04-07 08:52

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wanderlust', '0012_alter_trip_accommodation_type_alter_trip_travel_mode'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='accommodation_type',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('HOSTEL', 'Hostel'), ('AIRBNB', 'Airbnb'), ('CAMPSITE', 'Campsite'), ('OTHER', 'Other')], max_length=50, verbose_name='accommodation type'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='description',
            field=models.TextField(verbose_name='trip description'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(max_length=255, verbose_name='destination'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='estimated_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='estimated budget'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trip_images/', verbose_name='trip image'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='max_participants',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='maximum participants'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='title',
            field=models.CharField(max_length=100, verbose_name='trip title'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travel_mode',
            field=models.CharField(choices=[('AIRPLANE', 'Airplane'), ('CAR', 'Car'), ('TRAIN', 'Train'), ('BUS', 'Bus'), ('CRUISE', 'Cruise'), ('WALK', 'Walk'), ('MULTIPLE', 'Multiple')], max_length=50, verbose_name='travel mode'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='wanderlustuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
