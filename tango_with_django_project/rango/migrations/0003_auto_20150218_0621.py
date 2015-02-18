# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150218_0620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='lokes',
            new_name='likes',
        ),
    ]
