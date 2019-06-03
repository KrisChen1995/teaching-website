# _*_ coding: utf-8 _*_
__author__ = 'chenfei'
__date__ = '2018/12/11 15:20'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# method_decorator 用于转换装饰器，使得其能在类中使用
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)