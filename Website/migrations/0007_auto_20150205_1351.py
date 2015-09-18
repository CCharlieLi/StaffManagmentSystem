# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_auto_20150205_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
