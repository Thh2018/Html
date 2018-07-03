# coding=utf-8
from django.conf.urls import url
import views
urlpatterns = [
    # url(r'^$',views.login_view),
    url(r'^register/',views.register_view),
    url(r'^login/$', views.login_view),
    url(r'^isExist/',views.isExist_view),
    # url(r'^main/',views.login_view),
]