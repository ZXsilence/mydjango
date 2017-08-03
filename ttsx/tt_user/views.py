#coding=utf-8

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from models import *
from hashlib import sha1
from . import task
from PIL import Image, ImageDraw, ImageFont
import urllib
import urllib2
import time

import time
from datetime import date, datetime
import httplib

# def send(request):
#     # msg = '''
#     # <h1> hello world </h1>
#     #
#     # <a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>
#     #
#     # '''
#     #
#     # # msg = 'hello world'
#     # status =send_mail('账号激活','hello world',settings.EMAIL_FROM, ['451694791@qq.com'],html_message=msg)
#     #
#     # if status:
#     #     return HttpResponse('ok')
#     # else:
#     #     return HttpResponse('fail')
#     email = '906312371@qq.com'
#     task.send.delay(email)
#
#     return HttpResponse('ok')

def phone(request):

    data = {}
    header = {}

    url = 'https://api.netease.im/sms/sendcode.action'


    app_key = '3248b0b62615bfbec460386a86248721'
    app_secret = 'aa9436886336'
    nonce = '123456'
    cur_time = str(int(time.time()))
    print app_key+nonce+cur_time
    checksum = sha1(app_secret+nonce+cur_time).hexdigest()
    print checksum
    mobile = '18729242900'

    templateid = 3059844

    header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    header['AppKey'] = app_key
    header['CurTime'] = cur_time
    header['Nonce'] = nonce
    header['CheckSum'] = checksum


    data['templateid'] = templateid
    data['mobile'] = mobile






    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    req.add_header('Content-Type', "application/x-www-form-urlencoded;charset=utf-8")
    req.add_header('AppKey', app_key)
    req.add_header('CurTime', cur_time)
    req.add_header('Nonce', nonce)
    req.add_header('CheckSum', checksum)


    response = urllib2.urlopen(req)
    html = response.read()
    return HttpResponse(html)

def check(request):
    data = {}
    header = {}

    url = 'https://api.netease.im/sms/verifycode.action'

    app_key = '3248b0b62615bfbec460386a86248721'
    app_secret = 'aa9436886336'
    nonce = '123456'
    cur_time = str(int(time.time()))
    print app_key + nonce + cur_time
    checksum = sha1(app_secret + nonce + cur_time).hexdigest()
    print checksum
    mobile = '18729242900'

    templateid = 3059844

    header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    header['AppKey'] = app_key
    header['CurTime'] = cur_time
    header['Nonce'] = nonce
    header['CheckSum'] = checksum

    # data['templateid'] = templateid
    data['mobile'] = mobile
    data['code'] = 6991

    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    req.add_header('Content-Type', "application/x-www-form-urlencoded;charset=utf-8")
    req.add_header('AppKey', app_key)
    req.add_header('CurTime', cur_time)
    req.add_header('Nonce', nonce)
    req.add_header('CheckSum', checksum)

    response = urllib2.urlopen(req)
    html = response.read()
    return HttpResponse(html)



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

    task.send.delay(info.uemail)

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

    pwd = dict.get('pwd')

    pwd_sha1 = sha1(pwd).hexdigest()

    db_dict = UserInfo.objects.all()

    name_list = []
    pwd_list = []
    for temp in db_dict:
        name_list.append(temp.uname)
        pwd_list.append(temp.upwd)
    if name in name_list and pwd_sha1 in pwd_list:
        # path = request.session.get('url_path')
        print request.session
        # response.set_cookie('name', name)
        request.session['uname'] = name
        request.session.set_expiry(60*60*1)

        return render(request, 'tt_user/user_center_info.html', )
    else:
        context = {}
        context['name'] = name
        context['title'] = '登陆'
        # context['pwd'] = pwd
        context['error'] = 1

        return render(request, 'tt_user/login.html', context)



def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png

    # return HttpResponse(content= buf.getvalue(), content_type='image/png')
    return render(request, context = buf.getvalue(), content_type='image/png')



def center_info(request):


    return render(request, 'tt_user/user_center_info.html', )


def center_order(request):
    return render(request, 'tt_user/user_center_order.html')

def center_site(request):
    return render(request, 'tt_user/user_center_site.html')