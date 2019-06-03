# _*_ coding: utf-8 _*_
__author__ = 'chenfei'
__date__ = '2018/11/3 20:41'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']



class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums']
    list_filter = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)