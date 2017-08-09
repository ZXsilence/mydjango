from django.db import models
from tt_user.models import *
from tt_goods.models import *
# Create your models here.

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
