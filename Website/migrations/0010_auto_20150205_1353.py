# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0009_auto_20150205_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='GroupName',
            field=models.ForeignKey(to='Website.Group'),
        ),
    ]
