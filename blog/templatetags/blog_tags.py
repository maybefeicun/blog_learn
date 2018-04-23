# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 9:38
# @Author  : chen
# @File    : blog_tags.py
# @Software: PyCharm

from django import template
from ..models import Post, Category

# 这里的代码是按照Django的规定注册这个函数为模板标签
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    # 记住Mysql的接口语法
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    '''
    文档归类标签
    '''
    return Post.objects.dates('created_time', 'month', order="DESC")

@register.simple_tag
def get_categories():
    return Category.objects.all()

