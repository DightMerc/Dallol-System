from django.shortcuts import render, get_object_or_404

from .models import TelegramUser, TemporaryOrder, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, Order, Photo, OnlineRieltor, CommonRieltorUser, Agency


from django.db import IntegrityError

from datetime import date, timedelta, time, datetime
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import redirect

from django.http import JsonResponse, HttpResponse, response, HttpResponsePermanentRedirect
from .utils import OnlineGenerateEndText, GenerateEndText

from django.core.paginator import Paginator
from .forms import PostForm, PostForm2

from django.contrib.auth import authenticate, login, logout



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
                post.user = request.user

                agency = Agency.objects.get(user=request.user)
                agency.rieltors.add(OnlineRieltor.objects.get(id=post.id))

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


def OperationShowViewCommonAgency(request, operation, pk, telegram_user):
    if request.user.is_authenticated:
        if True:

            paginator = Paginator(Order.objects.filter(active=True).filter(type=str(operation)).filter(user=TelegramUser.objects.get(pk=telegram_user)), 15)

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
            return render(request, 'api/statisticsMoreCommonAgency.html', {
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


def OperationViewAgency(request, pk):
    if request.user.is_authenticated:
        if True:

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

def OperationShowViewAgency(request, operation, pk, rieltor):
    if request.user.is_authenticated:
        if True:
        
            paginator = Paginator(OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=OnlineRieltor.objects.get(id=rieltor)).filter(type=str(operation)), 15)

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
            return render(request, 'api/statisticsMoreAgency.html', {
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


def NewAnnView(request):
    if request.user.is_authenticated:
        if True:
            if request.method == "POST":
                form = PostForm2(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save()
                    post.user = request.user
                    post = form.save()


                    agency = Agency.objects.get(user=request.user)
                    agency.rieltors.add(OnlineRieltor.objects.get(id=post.id))

                    return redirect('/')


                else:
                    return HttpResponse(form.errors)
            else:

                form = PostForm2()
                return render(request, 'api/addAnn.html', {
                    'form': form,
                })
            
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def NewAgentView(request):
    if request.user.is_authenticated:
        if True:
            if request.method == "POST":
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save()
                    post.user = request.user
                    post = form.save()


                    agency = Agency.objects.get(user=request.user)
                    agency.rieltors.add(OnlineRieltor.objects.get(id=post.id))

                    return redirect('/')


                else:
                    return HttpResponse(form.errors)
            else:

                form = PostForm()
                return render(request, 'api/addAgent.html', {
                    'form': form,
                })
            
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")
    
def OperationViewCommonAgency(request, pk):
    if request.user.is_authenticated:
        if True:
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

            
            return render(request, 'api/admin.html', {
                "order": order,
                "text": text,
                
            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def OnlineStatViewAgencySingle(request, pk):
    week=date.today()-timedelta(days=7)

    today = date.today()

    rieltors = OnlineRieltor.objects.all()

    max = 0
    Top_rieltor = None
    for rieltor in rieltors:
        if OnlineRieltorOrder.objects.filter(rieltor=rieltor).count() > max:
            max = OnlineRieltorOrder.objects.filter(rieltor=rieltor).count()
            Top_rieltor = rieltor

    selected_rieltor = OnlineRieltor.objects.get(pk=pk)
    common_user = CommonRieltorUser.objects.get(rieltor=selected_rieltor)
    telegram_user = TelegramUser.objects.get(phone=int(common_user.user.username))

    
    if request.user.is_authenticated:
        # if CommonRieltorUser.objects.get(user__username=request.user).active:
            

        #     try:
        #         rieltor = TelegramUser.objects.get(phone=request.user.3)
        #     except Exception as e:
        #         return HttpResponse("Доступ разрешен только для риелторов. Войдите в учетную запись риелтора")
        if True:

            return render(request, 'api/statistics2agency.html', {
                "saleOrders": Order.objects.filter(active=True).filter(type="sale").filter(user=telegram_user),
                "rentOrders": Order.objects.filter(active=True).filter(type="rent").filter(user=telegram_user),

                "saleFlat": Order.objects.filter(active=True).filter(type="sale").filter(property="Квартира").filter(user=telegram_user),
                "saleLand": Order.objects.filter(active=True).filter(type="sale").filter(property="Участок земли").filter(user=telegram_user),
                "saleArea": Order.objects.filter(active=True).filter(type="sale").filter(property="Участок").filter(user=telegram_user),
                "saleFreeArea": Order.objects.filter(active=True).filter(type="sale").filter(property="Коммерческая недвижимость").filter(user=telegram_user),

                "rentFlat": Order.objects.filter(active=True).filter(type="rent").filter(property="Квартира").filter(user=telegram_user),
                "rentLand": Order.objects.filter(active=True).filter(type="rent").filter(property="Участок земли").filter(user=telegram_user),
                "rentArea": Order.objects.filter(active=True).filter(type="rent").filter(property="Участок").filter(user=telegram_user),
                "rentFreeArea": Order.objects.filter(active=True).filter(type="rent").filter(property="Коммерческая недвижимость").filter(user=telegram_user),

                "onlineRieltorSaleOrders": OnlineRieltorOrder.objects.filter(rieltor=selected_rieltor).filter(type="sale"),
                "onlineRieltorRentOrders": OnlineRieltorOrder.objects.filter(rieltor=selected_rieltor).filter(type="rent"),

                "onlineRieltor": selected_rieltor,
                "telegram_user": telegram_user.id,

                "onlineRieltoronlineRieltorsaleFlat": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="sale").filter(property="Квартира"),
                "onlineRieltorsaleLand": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="sale").filter(property="Участок земли"),
                "onlineRieltorsaleArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="sale").filter(property="Участок"),
                "onlineRieltorsaleFreeArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="sale").filter(property="Коммерческая недвижимость"),

                "onlineRieltorrentFlat": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="rent").filter(property="Квартира"),
                "onlineRieltorrentLand": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="rent").filter(property="Участок земли"),
                "onlineRieltorrentArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="rent").filter(property="Участок"),
                "onlineRieltorrentFreeArea": OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=selected_rieltor).filter(type="rent").filter(property="Коммерческая недвижимость"),

            })
        else:
            return HttpResponse("Доступ запрещён. Свяжитесь с администратором")
    else:

        return redirect("/accounts/login/")


def TryLoginView(request):
    password = request.POST.get('password')
    username = request.POST.get('login')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("ok")

    else:
        return HttpResponse("Доступ запрещён. Свяжитесь с администратором")






def OnlineMain(request):
    if request.user.is_authenticated:
        try:
            onliners = Agency.objects.get(user=request.user).rieltors
            saleOrders = 0
            rentOrders = 0

            saleFlat = 0
            saleLand = 0
            saleArea = 0
            saleFreeArea = 0

            rentFlat = 0
            rentLand = 0
            rentArea = 0
            rentFreeArea = 0
            for online in onliners.all():

                saleOrders += Order.objects.filter(active=True).filter(type="sale").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                rentOrders += Order.objects.filter(active=True).filter(type="rent").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()

                saleFlat += Order.objects.filter(active=True).filter(type="sale").filter(property="Квартира").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                saleLand += Order.objects.filter(active=True).filter(type="sale").filter(property="Участок земли").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                saleArea += Order.objects.filter(active=True).filter(type="sale").filter(property="Участок").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                saleFreeArea += Order.objects.filter(active=True).filter(type="sale").filter(property="Коммерческая недвижимость").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()

                rentFlat += Order.objects.filter(active=True).filter(type="rent").filter(property="Квартира").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                rentLand += Order.objects.filter(active=True).filter(type="rent").filter(property="Участок земли").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                rentArea += Order.objects.filter(active=True).filter(type="rent").filter(property="Участок").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                rentFreeArea += Order.objects.filter(active=True).filter(type="rent").filter(property="Коммерческая недвижимость").filter(user=TelegramUser.objects.get(phone=int(online.user.username))).count()
                salePercent = int(saleOrders*100/(saleOrders+rentOrders))
                rentPercent =  int(rentOrders*100/(saleOrders+rentOrders))
            
            return render(request, 'api/index.html', {
                    'onliners': onliners.all(),
                    'saleOrders': saleOrders,
                    'rentOrders': rentOrders,
                    'salePercent': salePercent,
                    'rentPercent': rentPercent,
                    'orders': saleOrders+rentOrders,


                    "saleFlat": saleFlat,
                    "saleLand": saleLand,
                    "saleArea": saleArea,
                    "saleFreeArea": saleFreeArea,

                    "rentFlat": rentFlat,
                    "rentLand": rentLand,
                    "rentArea": rentArea,
                    "rentFreeArea": rentFreeArea,
                    "agency": Agency.objects.get(user=request.user)

                })
        except Exception as e:
            
            return HttpResponse("Доступ разрешен только для агенств. Войдите в учетную запись агентства " + str(e))
            
    else:
        return redirect("/login/")

    
def LoginForm(request):
    return render(request, 'api/pages-login.html', {
                })

def AgentsView(request):
    return render(request, 'api/users.html', {
        "agency": Agency.objects.get(user=request.user)
                })

def AnnsView(request, operation):
    return render(request, 'api/admins.html', {
        "agency": Agency.objects.get(user=request.user),
        "orders": Order.objects.filter(active=True).filter(type=str(operation)).filter(user=TelegramUser.objects.get(phone=request.user.username)),
                "trigger": False,

                })

def TryLogoutView(request):

    if request.user is not None:
        logout(request)
        return redirect("/")



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

            
            return render(request, 'api/admins.html', {
                "order": order,
                "text": text,
                "trigger": True,
                
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

def OperationMoreViewAgency(request, operation, property, pk, rieltor):
    if request.user.is_authenticated:
        if True:

            paginator = Paginator(OnlineRieltorOrder.objects.filter(active=True).filter(rieltor=OnlineRieltor.objects.get(id=rieltor)).filter(type=str(operation)).filter(property=str(property)), 15)

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


def OperationMoreViewCommonAgency(request, operation, property, pk, telegram_user):
    if request.user.is_authenticated:
        if True:
            paginator = Paginator(Order.objects.filter(active=True).filter(type=str(operation)).filter(property=str(property)).filter(user=telegram_user), 15)

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
            return render(request, 'api/statisticsMoreCommonAgency.html', {
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