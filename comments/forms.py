# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 9:42
# @Author  : chen
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    '''
    这里的方法除了forms.Form外还有一个为forms.ModelForm
    如果事先设定好了数据库模型就直接使用forms.ModelForm这样会简单点
    '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']