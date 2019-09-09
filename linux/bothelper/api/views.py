from django.shortcuts import render, get_object_or_404

from .models import TelegramUser, TemporaryOrder, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, Order, Photo, OnlineRieltor


from django.db import IntegrityError

from datetime import date, timedelta, time, datetime
from django.utils import timezone
from django.db.models import Count

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



