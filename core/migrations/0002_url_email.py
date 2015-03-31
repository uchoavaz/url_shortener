# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='email',
            field=models.EmailField(max_length=75, default=1, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]
