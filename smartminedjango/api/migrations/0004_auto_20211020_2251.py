# Generated by Django 3.2.2 on 2021-10-20 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211020_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='env_exception',
            old_name='warn_id',
            new_name='warn_type',
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 20, 22, 51, 44, 377212), verbose_name='ειζΆι΄'),
        ),
    ]
