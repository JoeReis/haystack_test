# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_geo_distance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geo',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
