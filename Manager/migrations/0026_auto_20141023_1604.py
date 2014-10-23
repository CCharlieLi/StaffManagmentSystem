# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0025_salarybase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Picture',
            field=models.ImageField(default='no-img.png', upload_to='head'),
        ),
    ]
