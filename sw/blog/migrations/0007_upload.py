# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170607_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
