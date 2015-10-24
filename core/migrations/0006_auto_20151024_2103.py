# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_contact_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b'Mr.'), (1, b'Ms.'), (2, b'Mrs.'), (3, b'Dr.')]),
        ),
    ]
