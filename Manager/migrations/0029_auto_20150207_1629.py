# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0028_auto_20141023_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Picture',
            field=models.ImageField(default=b'no-img.png', upload_to=b'manage/img/head'),
        ),
    ]
