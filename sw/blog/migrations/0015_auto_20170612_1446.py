# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-12 05:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170612_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='font',
            options={'ordering': ['-id']},
        ),
    ]
