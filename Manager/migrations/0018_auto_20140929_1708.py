# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0017_auto_20140928_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='level',
            name='Levelname',
            field=models.CharField(max_length=20),
        ),
    ]
