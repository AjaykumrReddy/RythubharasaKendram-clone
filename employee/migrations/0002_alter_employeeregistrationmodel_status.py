# Generated by Django 3.2.13 on 2022-07-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregistrationmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
