# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0008_auto_20150205_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='GroupName',
            field=models.ForeignKey(null=True, blank=True, to='Website.Group'),
        ),
    ]
