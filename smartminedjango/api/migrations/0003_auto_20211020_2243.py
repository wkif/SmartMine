# Generated by Django 3.2.2 on 2021-10-20 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210925_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='env_warn_type',
            fields=[
                ('warn_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('warn_value', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': '环境预警类型表',
                'verbose_name_plural': '环境预警类型表',
                'db_table': '环境预警类型表',
            },
        ),
        migrations.CreateModel(
            name='person_illegel_type',
            fields=[
                ('illegel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': '人员违规操作类型',
                'verbose_name_plural': '人员违规操作类型',
                'db_table': '人员违规操作类型',
            },
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 20, 22, 43, 29, 167865), verbose_name='发送时间'),
        ),
        migrations.CreateModel(
            name='person_illegel_upload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上报时间')),
                ('device', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.specific_device')),
                ('illgel', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.person_illegel_type')),
                ('person', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'verbose_name': '人员违规操作上报',
                'verbose_name_plural': '人员违规操作上报',
                'db_table': '人员违规操作上报',
            },
        ),
        migrations.CreateModel(
            name='env_exception',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上报时间')),
                ('watch_value', models.CharField(default='', max_length=50)),
                ('warn_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.env_warn_type')),
            ],
            options={
                'verbose_name': '环境预警上报表',
                'verbose_name_plural': '环境预警上报表',
                'db_table': '环境预警上报表',
            },
        ),
    ]
