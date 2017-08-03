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
    url(r'^verify/$', verify_code),
    url(r'^center_info/$', center_info),
    url(r'^center_order/$', center_order),
    url(r'^center_site/$', center_site),
    url(r'^phone/$', phone),
    url(r'^check/$', check),

]
