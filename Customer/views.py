# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
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


def condition_all_view(request,ccid=0):
    if request.method =='GET':
        ccondition = CustomerCondition.objects.all()
        try:
            CustomerCondition.objects.filter(condition_id = ccid).delete()
            return HttpResponse('删除成功！')
        except:
            return render(request, 'customer_state_list.html', {'ccondition': ccondition})

def condition_add_view(request):
    if request.method=='GET':
        return render(request, 'customer_state_add.html')
    else:
        cnames =request.POST.get('cname')
        cexplans=request.POST.get('cexplan')
        if cnames !=''and cexplans !='':
            CustomerCondition.objects.create(condition_name=cnames, condition_explain=cexplans)
            return HttpResponse('添加成功！')
        else:
            return HttpResponse('添加不能为空！')

def type_all_view(request,tid=0):
    if request.method == "GET":
        customertype = CustomerType.objects.all()
        try:
            CustomerType.objects.get(type_id=tid).delete()
            return HttpResponse('删除成功！')
        except:
            return render(request, 'customer_type_list.html', {'customertype': customertype})




def type_add_view(request):
    if request.method == 'GET':
        return render(request,'customer_type_add.html')
    else:
        ctname = request.POST.get('ctname')
        if ctname !='':
            CustomerType.objects.create(type_name=ctname)
            return HttpResponse('添加成功！')
        else:
            return HttpResponse('添加不能为空！')


def source_list_view(request,csid=0):
    if request.method == 'GET':
        sourcelist = CustomerSource.objects.all()
    try:
        CustomerSource.objects.filter(source_id=csid).delete()
        return HttpResponse('删除成功！')
    except:
        return render(request,'customer_source_list.html',{'sourcelist':sourcelist})


def source_add_view(request):
    if request.method =='GET':
        return render(request,'customer_source_add.html')
    else:
        socname = request.POST.get('soname')
        if socname !='':
            CustomerSource.objects.create(source_name=socname)
            return HttpResponse('添加成功！')
        else:
            return HttpResponse('添加不能为空！')


