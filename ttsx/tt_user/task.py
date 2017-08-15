# -*- coding: utf-8 -*-

from celery import task
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery, platforms

platforms.C_FORCE_ROOT = True  #加上这一行

@task
def send(email):
    print 'sending...'
    msg = '''
    <h1> hello world </h1>

    <a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>

    '''

    # msg = 'hello world'
    status =send_mail('账号激活','',settings.EMAIL_FROM, [email],html_message=msg)
    if status:
        print 'ok'
    else:
        print 'fail'