# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
import json

# Create your views here.
def login_view(request):
    if request.method=='GET':
        # 2.判断客户端是否存在login对应的cookie信息
        if request.COOKIES.has_key('login'):
            # 3.获取login对应的cookie信息，login对应的value为uname,pwd
            login = request.COOKIES.get('login', '').split(',')
            # -------------------------------------------------> 解决中文编码问题3
            print('我是login：',login)
            uname = json.loads(login[0])
            pwd = login[1]
            return render(request, 'login.html', {'uname': uname, 'pwd': pwd})
        return render(request,'login.html')
    else:
        # 接收请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        if uname and pwd:
        #  查询数据库，并判断在数据库中是否只有一天匹配的信息
            c = Employee.objects.filter(ename=uname,epwd=pwd).count()
            if c == 1:
                # --------------------------------------------------------------------------------------------------------
                response = HttpResponse('登录成功')
                response.setdefault('Location', '/stu/mybase/')
                response.status_code = 302

                response.set_cookie('login', json.dumps(uname) + ',' + pwd, path='/stu/login/', max_age=24 * 60 * 60 * 3)
                # -------------------------------------------------------------------------------------------------------
                return response
            else:
                # return HttpResponse('登陆失败')
                return redirect('/stu/login/')
        return render(request,'login.html')

def isExist_view(request):
    # if request.method=='GET':
        # 接收请求参数
        uname = request.GET.get('uname', '')
        # 判断数据库中是否存在
        answer = Employee.objects.filter(ename=uname)
        # print('isExist')
        # print('my answer',answer)# 是个列表
        if answer:
            return JsonResponse({'flag':True})
        return JsonResponse({'flag':False})

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

def base_view(request):

    return render(request,'base.html')