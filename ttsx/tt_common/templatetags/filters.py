# -*- coding: utf-8 -*-

#引入注册对象
from django.template import Library
register=Library()

#使用装饰器进行注册
@register.filter
def page_list(page):


    paginator = page.paginator
    page_index = page.number

    if paginator.num_pages < 5:
        plist = paginator.page_range
    else:
        if page_index < 3:
            plist = paginator.page_range[0:5]
        elif page_index > paginator.num_pages - 3:
            plist = paginator.page_range[paginator.num_pages - 5:paginator.num_pages + 1]
        else:
            plist = paginator.page_range[page_index - 3:page_index + 2]
    return plist