# -*- coding: utf-8 -*-

from django.conf.urls import *
from views import *

urlpatterns = [
    url(r'^add/$', add),
    url(r'^$', cart),
    url(r'^delcart/$', delcart),
    url(r'^chcount/$', chcount),
    url(r'^count/$', count),
]
