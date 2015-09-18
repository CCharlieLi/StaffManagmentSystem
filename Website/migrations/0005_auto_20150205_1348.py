# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_auto_20150203_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='partnership',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='peopletype',
            name='Name',
            field=models.CharField(verbose_name='Type', max_length=100),
        ),
        migrations.AddField(
            model_name='people',
            name='GroupName',
            field=models.ForeignKey(default='', to='Website.Group'),
        ),
    ]
