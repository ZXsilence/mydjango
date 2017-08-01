#coding=utf-8

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.
from models import *
from hashlib import sha1





def user_login(request):
    context = {'title': '登陆'}
    return render(request, 'tt_user/login.html', context)



def index(request):
    return HttpResponse('ok')


def user_register(request):
    context = {'title': '注册'}
    return render(request, 'tt_user/register.html', context)


def user_info(request):
    dict = request.POST

    info = UserInfo()

    info.uname = dict.get('user_name')

    info.upwd = sha1(dict.get('pwd')).hexdigest()

    info.uemail = dict.get('email')

    info.save()


    return redirect('/user/login/')


def check_username(request):
    db_dict = UserInfo.objects.all()

    name_list = []
    for temp in db_dict:
        name_list.append(temp.uname)
    return JsonResponse( {'name_list': name_list})


def login_submit(request):
    dict = request.POST

    name = dict.get('username')

    pwd = sha1(dict.get('pwd')).hexdigest()

    db_dict = UserInfo.objects.all()

    name_list = []
    pwd_list = []
    for temp in db_dict:
        name_list.append(temp.uname)
        pwd_list.append(temp.upwd)
    if name in name_list and pwd in pwd_list:

        request.session['uname'] = name
        request.session.set_expiry(60*60*1)

        return HttpResponse('ok')
    else:
        return HttpResponse('fail')


