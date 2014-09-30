# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0008_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('UserID', models.CharField(max_length=20)),
                ('Score', models.CharField(blank=True, max_length=5, null=True)),
                ('Event', models.CharField(max_length=400)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='Score',
            field=models.CharField(blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
    ]
