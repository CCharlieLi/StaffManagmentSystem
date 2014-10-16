# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0019_auto_20141015_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='Datetime',
            field=models.CharField(max_length=20),
        ),
    ]
