# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0007_auto_20140810_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('UserID', models.CharField(default='charlie', max_length=20)),
                ('title', models.CharField(default='My Event', max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('start', models.CharField(null=True, blank=True, max_length=100)),
                ('end', models.CharField(null=True, blank=True, max_length=100)),
                ('allday', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
    ]
