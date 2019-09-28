from django.shortcuts import render, get_object_or_404

from .models import TelegramUser, TemporaryOrder, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, Order, Photo, OnlineRieltor, CommonRieltorUser


from django.db import IntegrityError

from datetime import date, timedelta, time, datetime
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import redirect

def StatView(request):

    week=date.today()-timedelta(days=7)

    today = date.today()

    rieltors = OnlineRieltor.objects.all()

    max = 0
    Top_rieltor = None
    for rieltor in rieltors:
        if OnlineRieltorOrder.objects.filter(rieltor=rieltor).count() > max:
            max = OnlineRieltorOrder.objects.filter(rieltor=rieltor).count()
            Top_rieltor = rieltor


    return render(request, 'api/index.html', {
       'users' : TelegramUser.objects.all(), 

       'last_week_users': TelegramUser.objects.filter(created_date__gte=week),
       'today_users': TelegramUser.objects.filter(created_date__day=today.day),

       'last_week_orders': Order.objects.filter(created_date__gte=week),
       'today_orders': Order.objects.filter(created_date__day=today.day),

       'Top_rieltor': Top_rieltor,


       'orders': Order.objects.all(),
       'online_orders': OnlineRieltorOrder.objects.all(),

       'last_week_online_orders': OnlineRieltorOrder.objects.filter(created_date__gte=week),
       'today_online_orders': OnlineRieltorOrder.objects.filter(created_date__day=today.day),

       'temp_orders': TemporaryOrder.objects.all(),
       'online_temp_orders': OnlineRieltorTemporaryOrder.objects.all(),
       'photoes':Photo.objects.all()})


def OnlineStatView(request):

    week=date.today()-timedelta(days=7)

    today = date.today()

    rieltors = OnlineRieltor.objects.all()

    max = 0
    Top_rieltor = None
    for rieltor in rieltors:
        if OnlineRieltorOrder.objects.filter(rieltor=rieltor).count() > max:
            max = OnlineRieltorOrder.objects.filter(rieltor=rieltor).count()
            Top_rieltor = rieltor


    if request.user.is_authenticated:
        return render(request, 'api/statistics.html', {
            "saleOrders": Order.objects.filter(active=True).filter(_type="sale"),
            "rentOrders": Order.objects.filter(active=True).filter(_type="rent"),

            "saleFlat": Order.objects.filter(active=True).filter(_type="sale").filter(_property="Квартира"),
            "saleLand": Order.objects.filter(active=True).filter(_type="sale").filter(_property="Участок земли"),
            "saleArea": Order.objects.filter(active=True).filter(_type="sale").filter(_property="Участок"),
            "saleFreeArea": Order.objects.filter(active=True).filter(_type="sale").filter(_property="Коммерческая недвижимость"),

            "rentFlat": Order.objects.filter(active=True).filter(_type="rent").filter(_property="Квартира"),
            "rentLand": Order.objects.filter(active=True).filter(_type="rent").filter(_property="Участок земли"),
            "rentArea": Order.objects.filter(active=True).filter(_type="rent").filter(_property="Участок"),
            "rentFreeArea": Order.objects.filter(active=True).filter(_type="rent").filter(_property="Коммерческая недвижимость"),

            "onlineRieltorSaleOrders": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="sale"),
            "onlineRieltorRentOrders": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="rent"),

            "onlineRieltor": CommonRieltorUser.objects.get(user__username=request.user).rieltor,

            "onlineRieltoronlineRieltorsaleFlat": OnlineRieltorOrder.objects.filter(active=True).filter(_type="sale").filter(_property="Квартира"),
            "onlineRieltorsaleLand": OnlineRieltorOrder.objects.filter(active=True).filter(_type="sale").filter(_property="Участок земли"),
            "onlineRieltorsaleArea": OnlineRieltorOrder.objects.filter(active=True).filter(_type="sale").filter(_property="Участок"),
            "onlineRieltorsaleFreeArea": OnlineRieltorOrder.objects.filter(active=True).filter(_type="sale").filter(_property="Коммерческая недвижимость"),

            "onlineRieltorrentFlat": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="rent").filter(_property="Квартира"),
            "onlineRieltorrentLand": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="rent").filter(_property="Участок земли"),
            "onlineRieltorrentArea": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="rent").filter(_property="Участок"),
            "onlineRieltorrentFreeArea": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(_type="rent").filter(_property="Коммерческая недвижимость"),

        })
    else:

        return redirect("/accounts/login/")
