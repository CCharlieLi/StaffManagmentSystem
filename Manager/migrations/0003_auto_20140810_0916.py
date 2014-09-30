# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_employee_levelname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('UserID', models.ForeignKey(to='Manager.Employee')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Publisher', models.CharField(max_length=20)),
                ('Datetime', models.DateField()),
                ('Content', models.TextField(blank=True)),
                ('Progress', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='QQ',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
