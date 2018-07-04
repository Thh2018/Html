# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'base.html')


def top_view(request):
    uname=request.GET.get('uname','')
    return render(request, 'top.html',{'uname':uname})


def left_view(request):
    return render(request, 'left.html')


def down_view(request):
    return render(request, 'down.html')


def cus1(request):
    return render(request, 'customer_list1.html')


def cus2(request):
    return render(request, 'customer_distribute.html')


def cus3(request):
    return render(request, 'customer_care_list.html')

def cus4(request):
    return render(request, 'customer_type_list.html')

def cus5(request):
    return render(request, 'customer_state_list.html')

def cus6(request):
    return render(request, 'customer_source_list.html')

def cus7(request):
    return render(request, 'down.html')

def cus8(request):
    return render(request, 'down.html')

def cus9(request):
    return render(request, 'down.html')

def cus10(request):
    return render(request, 'down.html')

def cus11(request):
    return render(request, 'down.html')

def cus12(request):
    return render(request, 'down.html')

def cus13(request):
    return render(request, 'down.html')

def cus14(request):
    return render(request, 'down.html')

def cus15(request):
    return render(request, 'down.html')


