# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        # 接收请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        if uname and pwd:
        #  查询数据库，并判断在数据库中是否只有一天匹配的信息
            c = Employee.objects.filter(ename=uname,epwd=pwd).count()
            if c == 1:
                return render(request,'base.html')
            else:
                # return HttpResponse('登陆失败')
                return redirect('/login/')


def isExist_view(request):
    if request.method=='GET':
        # 接收请求参数
        uname = request.GET.get('uname', '')
        # 判断数据库中是否存在
        answer = Employee.objects.filter(ename=uname)
        # print answer# 是个列表

        if answer:
            return JsonResponse({'flag':True})
        return JsonResponse({'flag':False})


# def isLogin_view(request):
#     uname1 = request.POST.get('uname', '')
#     pwd = request.POST.get('pwd', '')
#     if uname1 and pwd:
#         #  查询数据库，并判断在数据库中是否只有一天匹配的信息
#         co = Employee.objects.filter(ename=uname1, epwd=pwd).count()
#         if co == 1:
#             return JsonResponse({'flag1': True})
#         return JsonResponse({'flag1': False})
#


def register_view(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        if uname and pwd:
            employee = Employee(ename=uname,epwd=pwd)
            employee.save()
            return render(request,'login.html')

        return render(request,'register.html')