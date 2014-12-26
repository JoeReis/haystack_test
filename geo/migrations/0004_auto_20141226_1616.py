# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20141215_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geo',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='geo',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
