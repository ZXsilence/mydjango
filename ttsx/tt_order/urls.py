# -*- coding: utf-8 -*-
from django.conf.urls import *
from views import *
urlpatterns = [
    url(r'list/$', list),
    url(r'handle/$', handle),
]