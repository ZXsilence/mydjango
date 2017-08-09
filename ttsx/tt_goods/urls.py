# -*- coding: utf-8 -*-
from django.conf.urls import *
from views import *
urlpatterns = [
    url(r'^$', index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', list_goods ),
    url(r'^detail_(\d+)/$', detail ),
    # url(r'', ),
    # url(r'', ),
]