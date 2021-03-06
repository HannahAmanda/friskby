# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0016_sensor_post_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apikey', models.CharField(max_length=128)),
                ('sensor_id', models.CharField(max_length=128)),
                ('timestamp_recieved', models.DateTimeField()),
                ('timestamp_data', models.DateTimeField()),
                ('value', models.CharField(max_length=128)),
                ('extra_data', models.TextField()),
                ('parsed', models.BooleanField(default=False)),
            ],
        ),
    ]
