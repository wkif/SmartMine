# Generated by Django 3.2.2 on 2021-10-20 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211020_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person_illegel_upload',
            old_name='illgel',
            new_name='illegel_type',
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 20, 23, 2, 34, 96088), verbose_name='发送时间'),
        ),
    ]