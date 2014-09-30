# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0011_auto_20140903_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salary',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='Publisher',
            new_name='UserID',
        ),
        migrations.AddField(
            model_name='plan',
            name='Estimate',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
