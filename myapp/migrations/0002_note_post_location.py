# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20141215_0258'),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='post_location',
            field=models.ForeignKey(to='geo.Geo', null=True),
            preserve_default=True,
        ),
    ]
