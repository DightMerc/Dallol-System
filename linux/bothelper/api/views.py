from django.shortcuts import render, get_object_or_404

from .models import TelegramUser, TemporaryOrder, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, Order, Photo, OnlineRieltor


from django.db import IntegrityError

from datetime import date, timedelta, time, datetime
from django.utils import timezone

def StatView(request):

    week=date.today()-timedelta(days=7)

    today = date.today()

    rieltors = OnlineRieltor.objects.all()
    top_rieltors = OnlineRieltor.objects.annotate(order_count=Count('book')).order_by('-num_books')[:5]
    # https://docs.djangoproject.com/en/dev/topics/db/aggregation/
    

    return render(request, 'api/index.html', {
       'users' : TelegramUser.objects.all(), 

       'last_week_users': TelegramUser.objects.filter(created_date__gte=week),
       'today_users': TelegramUser.objects.filter(created_date__day=today.day),

       'last_week_orders': Order.objects.filter(created_date__gte=week),
       'today_orders': Order.objects.filter(created_date__day=today.day),

       'orders': Order.objects.all(),
       'online_orders': OnlineRieltorOrder.objects.all(),
       'temp_orders': TemporaryOrder.objects.all(),
       'online_temp_orders': OnlineRieltorTemporaryOrder.objects.all(),
       'photoes':Photo.objects.all()})



