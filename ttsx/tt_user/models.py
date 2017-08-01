from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    class Meta:
        db_table = 'userinfo'



class UserAddr(models.Model):
    addr = models.CharField(max_length=100, default='')
    reciever = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=11, default='')
    uname = models.ForeignKey('UserInfo')
    class Meta:
        db_table = 'useraddr'
