# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0018_auto_20140929_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='SalaryPoint',
            field=models.CharField(blank=True, max_length=5, null=True, default='0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='salary',
            name='SalaryPoint',
            field=models.CharField(blank=True, max_length=5, null=True, default='0'),
            preserve_default=True,
        ),
    ]
