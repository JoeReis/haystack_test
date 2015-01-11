# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_auto_20141226_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='geo',
            name='distance',
            field=models.CharField(max_length=4, default='5', choices=[('5', '5'), ('10', '10'), ('25', '25'), ('50', '50'), ('100', '100')]),
            preserve_default=True,
        ),
    ]
