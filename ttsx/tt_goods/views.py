#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import *
# Create your views here.


def index(request):
    type_list = TypeInfo.objects.all()
    list = []
    for typeinfo in type_list:
        list.append({
            'type':typeinfo,
            'list_new': typeinfo.goodsinfo_set.order_by('-id')[0:4],
            'list_click': typeinfo.goodsinfo_set.order_by('-gclick')[0:3],
        })

    context = {'title': '首页', 'list': list}
    return render(request, 'tt_goods/index.html', context)


def list_goods(request, id, page_index, select_type):

    page_index = int(page_index)
    type = TypeInfo.objects.get(id=id)

    list_new = type.goodsinfo_set.order_by('-id')[0:2]

    if select_type == '1':
        goods_list = type.goodsinfo_set.order_by('-id')
    if select_type == '2':
        goods_list = type.goodsinfo_set.order_by('gprice')
    if select_type == '3':
        goods_list = type.goodsinfo_set.order_by('-gclick')
    # print type.ttitle
    # goods_list = type.goodsinfo_set.order_by('-id')
    print goods_list
    paginator = Paginator(goods_list, 10 )

    page = paginator.page(page_index)



    if paginator.num_pages < 5:
        plist = paginator.page_range
    else:
        if page_index < 3:
            plist = paginator.page_range[0:5]
        elif page_index > paginator.num_pages - 3:
            plist = paginator.page_range[paginator.num_pages-5:paginator.num_pages+1]
        else:
            plist = paginator.page_range[page_index-3:page_index+2]



    context = {'title':type.ttitle, 'page':page, 'type':type, 'plist':plist, 'select_type': select_type, 'list_new': list_new}

    return render(request, 'tt_goods/list.html', context)


def detail(request, id):
    goods = GoodsInfo.objects.filter(id = id)
    goods = goods[0]

    goods.gclick += 1
    goods.save()
    new_list = GoodsInfo.objects.filter(gtype=goods.gtype).order_by('-id')[0:2]

    context = {'goods':goods, 'title': goods.gtitle, 'new_list':new_list}
    response = render(request, 'tt_goods/detail.html', context )

    goods_ids = request.COOKIES.get('goods_ids', '')
    if len(goods_ids) == 0:
        temp = [id]
        print id
    else:
        temp = goods_ids.split(',')
        if id in temp:
            temp.remove(id)
            temp.insert(0, id)
        else:
            temp.insert(0, id)
            if len(temp) > 5:
                temp.pop()
    response.set_cookie('goods_ids', ','.join(temp))


    return response