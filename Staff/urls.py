# coding= utf-8
from django.conf.urls import url

from Staff import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^top.html$', views.top_view),
    url(r'^left.html$', views.left_view),
    url(r'^down.html$', views.down_view),
    url(r'^Staff/1',views.ataff1),
    url(r'^Staff/2',views.ataff2),
    url(r'^Staff/3',views.ataff3),
    url(r'^Staff/4',views.ataff4),
    url(r'^Staff/5',views.ataff5),

]