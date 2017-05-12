# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-12 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170511_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5e7f\u544a\u6807\u9898')),
                ('img_url', models.ImageField(blank=True, default='ad/2017/05/9.jpg', max_length=200, null=True, upload_to='ad/%Y/%m', verbose_name='\u5e7f\u544a\u56fe\u7247')),
                ('redirect_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u8df3\u8f6c\u5730\u5740')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u53cb\u60c5\u94fe\u63a5')),
                ('url', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u8df3\u8f6c\u5730\u5740')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Strategic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u6218\u7565\u4f19\u4f34')),
                ('img_url', models.ImageField(blank=True, default='pa/2017/05/9.jpg', max_length=200, null=True, upload_to='pa/%Y/%m', verbose_name='logo')),
                ('redirect_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u8df3\u8f6c\u5730\u5740')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u6218\u7565\u5408\u4f5c\u4f19\u4f34',
                'verbose_name_plural': '\u6218\u7565\u5408\u4f5c\u4f19\u4f34',
            },
        ),
    ]