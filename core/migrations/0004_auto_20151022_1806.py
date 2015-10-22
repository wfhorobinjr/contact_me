# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151022_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
