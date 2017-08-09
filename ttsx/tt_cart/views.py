#coding=utf-8

from django.shortcuts import render


from django.http import JsonResponse
# Create your views here.
from models import *
from tt_user.models import *
from tt_cart.cart_decorators import *
from django.db.models import *


def add(request):
    dict = request.GET
    gid = int(dict.get('gid'))
    count = int(dict.get('count'))

    name = request.session.get('name', '')
    
    if name == '':
       return JsonResponse({'isok':0})
    user = UserInfo.objects.get(uname=name)
    cart = CartInfo.objects.filter(user = user, goods_id=gid)
    print cart
    if len(cart) == 0:
        cart = CartInfo()
        cart.user = user
        cart.goods_id = int(gid)
        cart.count = int(count)
        cart.save()
    else:
        cart = cart[0]

        cart.count+=count

        cart.save()

    return JsonResponse({'isok':1})



@user
def cart(request):
    name = request.session.get('name')
    cart_list = CartInfo.objects.filter(user=UserInfo.objects.get(uname=name)).order_by('-id')

    print cart_list
    context = {'title': '购物车', 'cart_list':cart_list}

    return render(request, 'tt_cart/cart.html' , context)


def delcart(request):
    try:

        cid = int(request.GET.get('cid'))

        cart = CartInfo.objects.get(id=cid)
        cart.delete()


        return JsonResponse({'isok': 1})
    except:
        return JsonResponse({'isok': 0})

def chcount(request):

    dict = request.GET
    cid = int(dict['cid'])
    count = int(dict['count'])
    print cid,count

    cart = CartInfo.objects.get(id=cid)
    cart.count = count
    cart.save()
    return JsonResponse({'isok': 1})


def count(request):
    name = request.session.get('name', 0)
    if name == 0:
        return JsonResponse({'isok':0})
    else:
        user = UserInfo.objects.get(uname=name)
        cart_count = CartInfo.objects.filter(user=user).aggregate(Sum('count'))
        print cart_count
        return JsonResponse({'isok':1, 'count':cart_count.get('count__sum')})