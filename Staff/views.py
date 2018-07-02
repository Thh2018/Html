# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base.html')


def top_view(request):
    return render(request, 'top.html')


def left_view(request):
    return render(request, 'left.html')


def down_view(request):
    return render(request, 'down.html')


def ataff1(request):
    return render(request,'dept_list.html')


def ataff2(request):
    return render(request, 'emp_list.html')


def ataff3(request):
    return render(request, 'house_list.html')


def ataff4(request):
    return render(request, 'house_type_list.html')


def ataff5(request):
    return render(request, 'notice_list.html')