# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-11 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_class_info_cls_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='job_title',
            field=models.CharField(max_length=50, null=True, verbose_name='\u804c\u79f0'),
        ),
    ]
