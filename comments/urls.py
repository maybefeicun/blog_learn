# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 14:17
# @Author  : chen
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]