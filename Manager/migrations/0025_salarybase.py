# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0024_plan_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salarybase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Base', models.CharField(max_length=20, blank=True, null=True, default='0')),
                ('Publisher', models.CharField(max_length=20, default='')),
                ('Datetime', models.CharField(max_length=20, default='')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
    ]
