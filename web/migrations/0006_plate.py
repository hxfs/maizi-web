# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-11 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_teacher_tea_img_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u677f\u5757\u540d\u79f0')),
            ],
        ),
    ]
