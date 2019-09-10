import os, sys

# from django.core.wsgi import get_wsgi_application
# from django.contrib.auth.models import User
# from django.utils import timezone
import django
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import shutil
# from django.conf import settings
 



proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + "/bothelper/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bothelper.settings")
sys.path.append(proj_path)

print(proj_path)
django.setup()

from api import models as api_models
from bot import models as bot_models

def GetToken():
    return bot_models.Setting.objects.get(pk=1).token

async def Search(_type, _property, price, region, room_count, area):

    order_list = api_models.Order.objects.all()

    order_list = order_list.filter(_type=_type)

    if _property!="":
        order_list = order_list.filter(_property=_property)
        if order_list.count()!=0:

            if price!="":
                if " " in price:
                    prices = price.split(" ")
                    filtered = order_list.filter(ammount__lte=int(prices[1]))
                    order_list = filtered
                    filtered = order_list.filter(ammount__gte=int(prices[0]))
                    order_list = filtered
                    
                else:

                    if int(price)!=100000:

                        filtered = order_list.filter(ammount__lte=int(price))
                        order_list = filtered

                    else:

                        filtered = order_list.filter(ammount__gte=int(price))
                        order_list = filtered
                
              

            if region!="":
                filtered = order_list.filter(region=region)
                order_list = filtered
            

            if room_count!="":
                filtered = order_list.filter(room_count=room_count)
                order_list = filtered


            if area!="":
                filtered = order_list.filter(area=area)
                order_list = filtered
            
        else:
            pass


        return Paginator(order_list.filter(active=True), 5)

def getUserLanguage(user):
    return str(api_models.TelegramUser.objects.get(telegram_id=int(user)).language)
    

async def getRieltorPhoto(person):
    return api_models.OnlineRieltor.objects.get(name=person).photo

async def getAllPhotoes():
    return api_models.OnlineRieltor.objects.get(name=person).photo

async def getRieltorDescription(person):
    return api_models.OnlineRieltor.objects.get(name=person).description
    
def createOnlineTemporaryOrder(user, data):
    order = api_models.OnlineRieltorTemporaryOrder()

    order.user = get_object_or_404(api_models.TelegramUser, telegram_id=user)
    order._type = data[0]
    order._property = data[1]
    order.title = data[2]
    order.region = data[3]
    order.reference = data[4]
    order.location_X = data[5].split(" ")[0]
    order.location_Y = data[5].split(" ")[1]
    order.room_count = data[6]
    order.square = data[7]
    order.area = data[8]
    order.state = data[9]
    order.ammount = data[10]
    order.add_info = data[11]
    order.contact = data[12]
    order.rieltor = get_object_or_404(api_models.OnlineRieltor, name=data[13])
    order.save()

    photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
    for photo in photoes:
        print(os.getcwd())
        path = os.getcwd().replace('bot', 'bothelper') + "/media/" + str(photo)
        print(path)
        shutil.move(os.getcwd()+"/Users/" + str(user)+"/" + str(photo), path)

        image = api_models.Photo()
        image.title = str(photo)
        image.photo = path
        image.save()
        order.photo.add(get_object_or_404(api_models.Photo, pk=image.id))

    return order.id
    
def createTemporaryOrder(user, data):
    order = api_models.TemporaryOrder()

    order.user = get_object_or_404(api_models.TelegramUser, telegram_id=user)
    order._type = data[0]
    order._property = data[1]
    order.title = data[2]
    order.region = data[3]
    order.reference = data[4]
    order.location_X = data[5].split(" ")[0]
    order.location_Y = data[5].split(" ")[1]
    order.room_count = data[6]
    order.square = data[7]
    order.area = data[8]
    order.state = data[9]
    order.ammount = data[10]
    order.add_info = data[11]
    order.contact = data[12]
    order.save()

    photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
    for photo in photoes:
        path = os.getcwd().replace('bot', 'bothelper') + "/media/" + str(photo)
        shutil.move(os.getcwd()+"/Users/" + str(user)+"/" + str(photo), path)

        image = api_models.Photo()
        image.title = str(photo)
        image.photo = path
        image.save()
        order.photo.add(get_object_or_404(api_models.Photo, pk=image.id))

    return order.id

async def CreateRealOrder(num):
    temp = api_models.TemporaryOrder.objects.get(pk=num)
    order = api_models.Order()

    order.user = temp.user
    order._type = temp._type
    order._property = temp._property
    order.title = temp.title
    order.region = temp.region
    order.reference = temp.reference
    order.location_X = temp.location_X
    order.location_Y = temp.location_Y
    order.room_count = temp.room_count
    order.square = temp.square
    order.area = temp.area
    order.state = temp.state
    order.ammount = temp.ammount
    order.add_info = temp.add_info
    order.contact = temp.contact

    order.pro_order = temp

    order.save()

    for photo in temp.photo.all():
        order.photo.add(photo)

    return order.id

async def CreateRealOnlineOrder(num):
    temp = api_models.OnlineRieltorTemporaryOrder.objects.get(pk=num)
    order = api_models.OnlineRieltorOrder()

    order.rieltor = temp.rieltor
    order.user = temp.user
    order._type = temp._type
    order._property = temp._property
    order.title = temp.title
    order.region = temp.region
    order.reference = temp.reference
    order.location_X = temp.location_X
    order.location_Y = temp.location_Y
    order.room_count = temp.room_count
    order.square = temp.square
    order.area = temp.area
    order.state = temp.state
    order.ammount = temp.ammount
    order.add_info = temp.add_info
    order.contact = temp.contact

    order.pro_order = temp

    order.save()

    for photo in temp.photo.all():
        order.photo.add(photo)

    return order.id
    

def GetLastAnnouncment():
    return len(api_models.Order.objects.all())

async def getAdmin():
    _list = []
    for user in bot_models.Admin.objects.get(pk=1).user.all():
        _list.append(user.telegram_id)
    return _list


def getMessage(number):
    return bot_models.Message.objects.get(number=number)

def getRegions():
    return bot_models.Region.objects.all()

def GetLastAnnouncment():
    return api_models.Order.objects.all().count() + 1

def userExsists(user):
    try:
        api_models.TelegramUser.objects.get(telegram_id=int(user))
        return True
    except Exception as identifier:
        return False

def userCreate(user):
    new_user = api_models.TelegramUser()

    new_user.telegram_id = user.id
    new_user.full_name = user.full_name
    new_user.username = user.username

    new_user.save()

    return True

def getUser(user):
    try:
        api_models.TelegramUser.objects.get(telegram_id=int(user))
        return api_models.TelegramUser.objects.get(telegram_id=int(user))
    except Exception as identifier:
        return False


def userSetLanguage(user, language):
    
    current_user = api_models.TelegramUser.objects.get(telegram_id=int(user))
    current_user.language = language

    current_user.save()

def getAllOnline():
    return api_models.OnlineRieltor.objects.all()
