# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0022_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, default='', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='QQ',
            field=models.CharField(blank=True, max_length=20, default='', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Tel',
            field=models.CharField(blank=True, max_length=11, default='', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='UserName',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
