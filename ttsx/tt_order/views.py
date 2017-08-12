#coding=utf-8
from django.shortcuts import render,redirect
from tt_user.models import *
from tt_cart.models import *
from django.db import transaction
from models import *
from datetime import *
# Create your views here.



def list(request):
    context={'title':'提交订单'}
    name = request.session['name']
    user = UserInfo.objects.get(uname=name)
    context['useraddr'] = user.useraddr_set.all()[0]

    dict = request.POST
    cid_list = dict.getlist('cid')
    cart_list = CartInfo.objects.filter(id__in=cid_list)
    print cart_list
    context['cart_list'] = cart_list

    return render(request, 'tt_order/place_order.html', context)

@transaction.atomic
def handle(request):
    sid = transaction.savepoint()
    try:
        name = request.session.get('name')
        user = UserInfo.objects.get(uname=name)
        cids = request.POST.getlist('cid')
        order = OrderInfo()
        order.oid = '%s%d' % (datetime.now().strftime('%Y%m%d%H%M%S'),user.id)
        print user.id
        order.user = user
        print user
        order.ototal = 0
        order.oaddress = request.POST.get('address')
        order.save()


        cart_list = CartInfo.objects.filter(user=user)
        total=0
        for cart in cart_list:

            if cart.count>cart.goods.gkucun:
                transaction.savepoint_rollback(sid)
                return redirect('/cart/')
            else:
                print 1
                detail = OrderDetailInfo()
                detail.goods = cart.goods
                detail.order = order

                detail.price = cart.goods.gprice
                detail.count = cart.count
                detail.save()
                goods = cart.goods
                goods.gkucun -= cart.count
                goods.save()
                total+=detail.price*detail.count
                cart.delete()
        order.ototal = total
        order.save()
        transaction.savepoint_commit(sid)
        return redirect('/user/center_order/')
    except:
        transaction.savepoint_rollback(sid)
        return render(request,'/cart/')