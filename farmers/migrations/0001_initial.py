# Generated by Django 3.2.13 on 2022-07-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('login_id', models.CharField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=120)),
                ('aadhar_no', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'FarmerRegistration',
            },
        ),
    ]
