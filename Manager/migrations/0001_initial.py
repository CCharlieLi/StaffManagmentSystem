# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Title', models.CharField(max_length=100)),
                ('Datetime', models.DateField()),
                ('Content', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('UserID', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=20)),
                ('Picture', models.ImageField(upload_to='head', blank=True, null=True)),
                ('Tel', models.CharField(blank=True, null=True, max_length=11)),
                ('Email', models.EmailField(blank=True, null=True, max_length=254)),
                ('QQ', models.IntegerField(blank=True, null=True, max_length=20)),
                ('Other', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='announcement',
            name='Publisher',
            field=models.ForeignKey(to='Manager.Employee', blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='GroupName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=20)),
                ('GroupMaster', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='GroupName',
            field=models.ForeignKey(to='Manager.GroupName', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Levelname', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
