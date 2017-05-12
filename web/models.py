# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30, verbose_name=u'分类名称')
    category_num = models.IntegerField('显示课程编号(从小到大)', default=100)

    class Meta:
        verbose_name = '课程分类'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.category_name


class Teacher(models.Model):
    username = models.CharField(max_length=20, verbose_name=u'老师姓名')
    introduction = models.CharField(max_length=300, verbose_name=u'自我介绍')
    job_title = models.CharField(max_length=50, verbose_name=u'职称', null=True, default=u'无')
    tea_img_url = models.ImageField(upload_to='avatar/%Y/%m', default='course/12.png', max_length=200, blank=True, null=True, verbose_name=u'老师头像')

    class Meta:
        verbose_name = '老师姓名'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.username


class class_info(models.Model):
    cls_name = models.CharField(max_length=30, verbose_name=u'课程名称')
    cls_num = models.IntegerField('显示课程编号(从小到大)', default=100)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, verbose_name=u'老师姓名')
    cls_date = models.DateTimeField(auto_now_add=True, verbose_name=u'课程上架时间')
    cls_desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    category_name = models.ForeignKey(Category, blank=True, null=True, verbose_name=u'分类名称')
    cls_img_url = models.ImageField(upload_to='course/%Y/%m', default='course/12.png', max_length=200, blank=True, null=True, verbose_name='课程图片')

    class Meta:
        verbose_name = '课程名称'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.cls_name


class User(AbstractUser):
    nickname = models.CharField(max_length=20, verbose_name=u'昵称')
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    SEX = (
        ('M', 'Man'),
        ('W', 'Woman'),
        ('D', 'Demon'),
    )
    sex = models.CharField(max_length=1, choices=SEX, verbose_name=u'性别')
    member = models.BooleanField(default=False)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.nickname


class Plate(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'板块名称')

    class Meta:
        verbose_name = '板块名称'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    plate = models.ForeignKey(Plate, blank=True, null=True, verbose_name='分类')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


class Ad(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"广告标题")
    img_url = models.ImageField(upload_to='ad/%Y/%m', default='ad/2017/05/9.jpg', max_length=200, blank=True, null=True, verbose_name='广告图片')
    redirect_url = models.URLField(max_length=100, blank=True, null=True, verbose_name='跳转地址')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name

class Strategic(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"战略伙伴")
    img_url = models.ImageField(upload_to='pa/%Y/%m', default='pa/2017/05/9.jpg', max_length=200, blank=True, null=True, verbose_name='logo')
    redirect_url = models.URLField(max_length=100, blank=True, null=True, verbose_name='跳转地址')

    class Meta:
        verbose_name = '战略合作伙伴'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"友情链接")
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='跳转地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name

