# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-10 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_info',
            name='cls_img_url',
            field=models.ImageField(blank=True, default='course/12.png', max_length=200, null=True, upload_to='course/%Y/%m', verbose_name='\u8bfe\u7a0b\u56fe\u7247'),
        ),
    ]
