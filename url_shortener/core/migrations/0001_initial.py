# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_url', models.TextField(verbose_name='Url')),
                ('short_url', models.TextField(verbose_name='Url encurtado')),
                ('is_protected', models.BooleanField(verbose_name='Protegido ?', default=False)),
                ('url_password', models.CharField(verbose_name='Senha', max_length=20, blank=True)),
                ('slug', models.SlugField(verbose_name='Atalho')),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
                'ordering': ['original_url'],
            },
            bases=(models.Model,),
        ),
    ]
