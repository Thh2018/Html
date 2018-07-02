# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'base.html')


def top_view(request):
    return render(request, 'top.html')


def left_view(request):
    return render(request, 'left.html')


def down_view(request):
    return render(request, 'down.html')


def add1(request):
    return render(request, 'dept_add.html')


def add2(request):
    return render(request, 'emp_add.html')


def add3(request):
    return render(request, 'role_add.html')