# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0026_auto_20141023_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=10, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employee',
            name='Picture',
            field=models.ImageField(default='no-img.png', upload_to='img/head'),
        ),
    ]
