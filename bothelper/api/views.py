from django.shortcuts import render, get_object_or_404

from .models import TelegramUser, TemporaryOrder, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, Order, Photo, OnlineRieltor, CommonRieltorUser


from django.db import IntegrityError

from datetime import date, timedelta, time, datetime
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import redirect

from django.http import JsonResponse, HttpResponse, response, HttpResponsePermanentRedirect
from .utils import OnlineGenerateEndText, GenerateEndText

from django.core.paginator import Paginator
from .forms import PostForm, PostForm2


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


def OnlineAccountView(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                return redirect('/')

            else:
                return HttpResponse(form.errors)
        else:

            form = PostForm()
            return render(request, 'api/account.html', {
                    'form': form,
                })
    else:
        return redirect("/accounts/login/")


def OnlineAccountView(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                return redirect('/')

            else:
                return HttpResponse(form.errors)
        else:

            form = PostForm()
            return render(request, 'api/account.html', {
                    'form': form,
                })
    else:
        return redirect("/accounts/login/")


def OnlineMain(request):
    if request.user.is_authenticated:
        
        return render(request, 'api/common.html', {
                'onliners': OnlineRieltor.objects.filter(user=request.user),
            })
    else:
        return redirect("/accounts/login/")


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
        if CommonRieltorUser.objects.get(user__username=request.user).active:
            

            try:
                rieltor = TelegramUser.objects.get(phone=request.user.username)
            except Exception as e:
                return HttpResponse("Доступ разрешен только для риелторов. Войдите в учетную запись риелтора")


            return render(request, 'api/statistics.html', {
                "saleOrders": Order.objects.filter(active=True).filter(type="sale").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "rentOrders": Order.objects.filter(active=True).filter(type="rent").filter(user=TelegramUser.objects.get(phone=request.user.username)),

                "saleFlat": Order.objects.filter(active=True).filter(type="sale").filter(property="Квартира").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "saleLand": Order.objects.filter(active=True).filter(type="sale").filter(property="Участок земли").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "saleArea": Order.objects.filter(active=True).filter(type="sale").filter(property="Участок").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "saleFreeArea": Order.objects.filter(active=True).filter(type="sale").filter(property="Коммерческая недвижимость").filter(user=TelegramUser.objects.get(phone=request.user.username)),

                "rentFlat": Order.objects.filter(active=True).filter(type="rent").filter(property="Квартира").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "rentLand": Order.objects.filter(active=True).filter(type="rent").filter(property="Участок земли").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "rentArea": Order.objects.filter(active=True).filter(type="rent").filter(property="Участок").filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "rentFreeArea": Order.objects.filter(active=True).filter(type="rent").filter(property="Коммерческая недвижимость").filter(user=TelegramUser.objects.get(phone=request.user.username)),

                "onlineRieltorSaleOrders": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="sale"),
                "onlineRieltorRentOrders": OnlineRieltorOrder.objects.filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="rent"),

                "onlineRieltor": CommonRieltorUser.objects.get(user__username=request.user).rieltor,

                "onlineRieltoronlineRieltorsaleFlat": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="sale").filter(property="Квартира"),
                "onlineRieltorsaleLand": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="sale").filter(property="Участок земли"),
                "onlineRieltorsaleArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="sale").filter(property="Участок"),
                "onlineRieltorsaleFreeArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="sale").filter(property="Коммерческая недвижимость"),

                "onlineRieltorrentFlat": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="rent").filter(property="Квартира"),
                "onlineRieltorrentLand": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="rent").filter(property="Участок земли"),
                "onlineRieltorrentArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="rent").filter(property="Участок"),
                "onlineRieltorrentFreeArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type="rent").filter(property="Коммерческая недвижимость"),

            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def OperationMoreView(request, operation, property, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:

            paginator = Paginator(OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type=str(operation)).filter(property=str(property)), 15)

            page_count = []
            a = 0
            while a<paginator.num_pages:
                a += 1
                page_count.append(int(a))


            if not pk in page_count:
                return HttpResponse("Page not found", status=404)
                
            next_page = "#"
            prev_page = "#"

            if pk>1:
                prev_page = str(pk - 1)
            else:
                prev_page = "#"

            if pk + 1 > paginator.num_pages:
                next_page = "#"
            else:
                next_page = str(pk + 1)


            current_page = pk
            return render(request, 'api/statisticsMore.html', {
                "orders": paginator.page(current_page).object_list,
                "page_count":page_count, 
                "current_page": current_page, 
                "prev":prev_page, 
                "next":next_page,
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def OperationMoreViewCommon(request, operation, property, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:
            paginator = Paginator(Order.objects.filter(active=True).filter(type=str(operation)).filter(property=str(property)).filter(user=TelegramUser.objects.get(phone=request.user.username)), 15)

            page_count = []
            a = 0
            while a<paginator.num_pages:
                a += 1
                page_count.append(int(a))


            if not pk in page_count:
                return HttpResponse("Page not found", status=404)
                
            next_page = "#"
            prev_page = "#"

            if pk>1:
                prev_page = str(pk - 1)
            else:
                prev_page = "#"

            if pk + 1 > paginator.num_pages:
                next_page = "#"
            else:
                next_page = str(pk + 1)


            current_page = pk
            return render(request, 'api/statisticsMoreCommon.html', {
                "orders": paginator.page(current_page).object_list,
                "page_count":page_count, 
                "current_page": current_page, 
                "prev":prev_page, 
                "next":next_page,
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def OperationView(request, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:

            order = OnlineRieltorOrder.objects.get(pk=pk)
            location = f"{order.location_X} {order.location_X}"
            data = []
            data.append(order.type)
            data.append(order.property)
            data.append(order.title)
            data.append(order.region)
            data.append(order.reference)
            data.append(location)
            data.append(order.room_count)
            data.append(order.square)
            data.append(order.area)
            data.append(order.state)
            data.append(order.ammount)
            data.append(order.add_info)
            data.append(order.contact)
            data.append(order.main_floor)
            data.append(order.floor)
            data.append(order.rieltor)
            data.append(order.main_state)



            text = OnlineGenerateEndText(data)

            
            return render(request, 'api/statisticsSingle.html', {
                "order": order,
                "text": text,
                
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")

def OperationViewCommon(request, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:
            order = Order.objects.get(pk=pk)
            location = f"{order.location_X} {order.location_X}"
            data = []
            data.append(order.type)
            data.append(order.property)
            data.append(order.title)
            data.append(order.region)
            data.append(order.reference)
            data.append(location)
            data.append(order.room_count)
            data.append(order.square)
            data.append(order.area)
            data.append(order.state)
            data.append(order.ammount)
            data.append(order.add_info)
            data.append(order.contact)
            data.append(order.main_floor)
            data.append(order.floor)



            text = GenerateEndText(data)

            
            return render(request, 'api/statisticsSingle.html', {
                "order": order,
                "text": text,
                
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")





def OperationShowView(request, operation, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:
        
            paginator = Paginator(OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=CommonRieltorUser.objects.get(user__username=request.user).rieltor).filter(type=str(operation)), 15)

            page_count = []
            a = 0
            while a<paginator.num_pages:
                a += 1
                page_count.append(int(a))


            if not pk in page_count:
                return HttpResponse("Page not found", status=404)
                
            next_page = "#"
            prev_page = "#"

            if pk>1:
                prev_page = str(pk - 1)
            else:
                prev_page = "#"

            if pk + 1 > paginator.num_pages:
                next_page = "#"
            else:
                next_page = str(pk + 1)


            current_page = pk
            return render(request, 'api/statisticsMore.html', {
                "orders": paginator.page(current_page).object_list,
                "page_count":page_count, 
                "current_page": current_page, 
                "prev":prev_page, 
                "next":next_page,
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
        
    else:

        return redirect("/accounts/login/")


def OperationShowViewCommon(request, operation, pk):
    if request.user.is_authenticated:
        if CommonRieltorUser.objects.get(user__username=request.user).active:

            paginator = Paginator(Order.objects.filter(active=True).filter(type=str(operation)).filter(user=TelegramUser.objects.get(phone=request.user.username)), 15)

            page_count = []
            a = 0
            while a<paginator.num_pages:
                a += 1
                page_count.append(int(a))


            if not pk in page_count:
                return HttpResponse("Page not found", status=404)
                
            next_page = "#"
            prev_page = "#"

            if pk>1:
                prev_page = str(pk - 1)
            else:
                prev_page = "#"

            if pk + 1 > paginator.num_pages:
                next_page = "#"
            else:
                next_page = str(pk + 1)


            current_page = pk
            return render(request, 'api/statisticsMoreCommon.html', {
                "orders": paginator.page(current_page).object_list,
                "page_count":page_count, 
                "current_page": current_page, 
                "prev":prev_page, 
                "next":next_page,
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
        
    else:

        return redirect("/accounts/login/")


def InactiveCommonView(request, pk):
    if request.user.is_authenticated:
        if Order.objects.get(pk=pk).user == TelegramUser.objects.get(phone=request.user.username):
            order = Order.objects.get(pk=pk)
            order.active = False
            order.save()
            return HttpResponse("OK")

        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")