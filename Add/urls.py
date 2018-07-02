# coding= utf-8
from django.conf.urls import url

from Add import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^top.html$', views.top_view),
    url(r'^left.html$', views.left_view),
    url(r'^down.html$', views.down_view),
    url(r'^add/1',views.add1),
    url(r'^add/2',views.add2),
    url(r'^add/3',views.add3),

]
