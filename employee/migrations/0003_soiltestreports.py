# Generated by Django 3.2.13 on 2022-07-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employeeregistrationmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilTestReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('tracking_id', models.CharField(max_length=16)),
                ('test_reports', models.FileField(upload_to='reports/')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
