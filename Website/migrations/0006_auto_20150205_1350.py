# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_auto_20150205_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='GroupName',
            field=models.ForeignKey(to='Website.Group'),
        ),
    ]
