# coding= utf-8
from django.conf.urls import url

from Customer import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^top.html$', views.top_view),
    url(r'^left.html$', views.left_view),
    url(r'^down.html$', views.down_view),
    url(r'^Customer/1',views.cus1),
    url(r'^Customer/2',views.cus2),
    url(r'^Customer/3',views.cus3),
    url(r'^Customer/4',views.cus4),
    url(r'^Customer/5',views.cus5),
    url(r'^Customer/6',views.cus6),
    url(r'^Customer/7',views.cus7),
    url(r'^Customer/8',views.cus8),
    url(r'^Customer/9',views.cus9),
    url(r'^Customer/10',views.cus10),
    url(r'^Customer/11',views.cus11),
    url(r'^Customer/12',views.cus12),
    url(r'^Customer/13',views.cus13),
    url(r'^Customer/14',views.cus14),
    url(r'^Customer/15',views.cus15),

]
