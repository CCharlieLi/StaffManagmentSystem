# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Publsh_Date', models.DateField(auto_now=True)),
                ('Image', models.ImageField(verbose_name='Image(700x240)', upload_to='images', blank=True, null=True)),
                ('Content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('File', models.FileField(upload_to='file', blank=True, null=True)),
                ('Publsh_Date', models.DateField(auto_now=True)),
                ('keyword', models.CharField(max_length=100, blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Publsh_Date', models.DateField(auto_now=True)),
                ('Image', models.ImageField(verbose_name='Image(700x240)', upload_to='images', blank=True, null=True)),
                ('Content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(verbose_name='Image(700x240)', upload_to='images', blank=True, null=True)),
                ('Link', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Peole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Level', models.CharField(max_length=200)),
                ('Content', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(verbose_name='Image(220x220/220x140)', upload_to='images', blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('File', models.FileField(upload_to='file', blank=True, null=True)),
                ('Publsh_Date', models.DateField(auto_now=True)),
                ('keyword', models.CharField(max_length=100, blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='peole',
            name='Type',
            field=models.ForeignKey(to='Website.Type'),
        ),
        migrations.AddField(
            model_name='partnership',
            name='Type',
            field=models.ForeignKey(to='Website.Type'),
        ),
    ]
