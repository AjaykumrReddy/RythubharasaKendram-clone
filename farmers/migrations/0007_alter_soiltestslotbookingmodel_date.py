# Generated by Django 3.2.13 on 2022-07-06 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0006_auto_20220706_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soiltestslotbookingmodel',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 6, 12, 51, 53, 921535)),
        ),
    ]
