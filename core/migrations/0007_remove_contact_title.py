# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151024_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
    ]
