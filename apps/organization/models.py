# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime


from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
            return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    tag = models.CharField(default="全国知名", max_length=10, verbose_name=u'机构标签')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u'封面', max_length=100)
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    category = models.CharField(default="pxjg", verbose_name=u'机构类别', max_length=20,
                                choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")))
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取课程机构的教师数量
        return self.teacher_set.all().count()

    def __unicode__(self):
            return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    work_year = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    age = models.IntegerField(default=20, verbose_name=u'年龄')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    image = models.ImageField(default='',upload_to="teacher/%Y/%m", verbose_name=u'头像', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
            return self.name

    def get_course_nums(self):
        # 获取课程数量
        return self.course_set.all().count()