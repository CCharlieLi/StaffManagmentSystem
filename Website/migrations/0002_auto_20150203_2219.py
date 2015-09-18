# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Name', models.CharField(max_length=100)),
                ('Level', models.CharField(max_length=200)),
                ('Content', models.TextField(null=True, blank=True)),
                ('Image', models.ImageField(blank=True, verbose_name='Image(220x220/220x140)', upload_to='images', null=True)),
                ('Type', models.ForeignKey(to='Website.Type')),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.RemoveField(
            model_name='peole',
            name='Type',
        ),
        migrations.DeleteModel(
            name='Peole',
        ),
    ]
