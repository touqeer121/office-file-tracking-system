# Generated by Django 3.1.2 on 2020-10-01 20:12

import django.contrib.auth.password_validation
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid Mobile Number', regex='[0-9]{10}')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('registration_number', models.CharField(blank=True, max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid Registration Number', regex='[a-zA-Z]{2}[0-9]{5}')], verbose_name='Registration number')),
                ('admin', models.CharField(default='N', max_length=1)),
                ('password', models.CharField(max_length=128, validators=[django.contrib.auth.password_validation.validate_password], verbose_name='password')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff status')),
                ('image', models.ImageField(default='download.jpg', upload_to='profile/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
