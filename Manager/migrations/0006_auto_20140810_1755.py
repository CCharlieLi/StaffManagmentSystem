# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_calendar_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='Allday',
            new_name='allday',
        ),
        migrations.RenameField(
            model_name='calendar',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='calendar',
            old_name='End',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='calendar',
            old_name='Start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='calendar',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='calendar',
            old_name='UserID',
            new_name='userID',
        ),
    ]
