# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Levelname',
            field=models.ForeignKey(null=True, to='Manager.Level'),
            preserve_default=True,
        ),
    ]
