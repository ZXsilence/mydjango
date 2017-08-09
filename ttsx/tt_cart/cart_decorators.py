# -*- coding: utf-8 -*-
from django.shortcuts import redirect


def user(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('name',0):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return wrapper
