# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_auto_20150112_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geo',
            name='distance',
        ),
    ]
