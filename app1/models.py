# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class UserIPInfo(models.Model):
    ip = models.CharField(max_length=400,default='',verbose_name=u'ip地址',null=True)
    time = models.DateTimeField(verbose_name=u'更新时间',auto_now=True)
    port = models.CharField(max_length=10000, default='', verbose_name=u'端口信息', null=True)
    class Meta:
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = "useripinfo"

class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=10000, default='', verbose_name=u'用户浏览器信息', null=True)
    userip = models.CharField(max_length=2560, verbose_name=u'唯一设备ID', default="")

    # port = models.CharField(max_length=10000, default='', verbose_name=u'端口信息', null=True)

    userip = models.ForeignKey("UserIPInfo",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'用户浏览器信息表'
        verbose_name_plural = verbose_name
        db_table = "browseinfo"

