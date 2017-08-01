# -*- coding: utf-8 -*-

from django.conf.urls import *

from views import *

urlpatterns = [



    url(r'^login/$', user_login),
    url(r'^login_submit/$', login_submit),
    url(r'^register/$', user_register),
    url(r'^user_info/$', user_info),
    url(r'^check_username/$', check_username),
    # url(r'^send/$', send)
]
