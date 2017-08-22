# coding=utf8

from django.conf.urls import url
import adminapp.views as views

urlpatterns = [

    url(r'index',view=views.index),
    url(r'admin',view=views.admin),
    url(r'account',views.account)

]