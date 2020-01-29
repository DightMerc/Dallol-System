import os, sys
import psycopg2

# from django.core.wsgi import get_wsgi_application
# from django.contrib.auth.models import User
# from django.utils import timezone
import django
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import shutil
# from django.conf import settings




import sqlalchemy


 



proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + "/bothelper/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bothelper.settings")
sys.path.append(proj_path)

print(proj_path)
django.setup()

from api import models as api_models
from bot import models as bot_models
from django.contrib.auth.models import User


def GetToken():
    return bot_models.Setting.objects.get(pk=1).token


def connect():
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format("postgres", "secret", "185.159.129.94", "5432", "dallolcrm_db")

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

def TryMigrate():
    print("Try migrate...")

    con, META_DATA = connect()

    connection = con.connect()

    myTable = sqlalchemy.Table('advert_adverts', META_DATA, autoload=True, autoload_with=con)

    orders = api_models.Order.objects.all()

    sales = {
        "Коммерческая недвижимость": 20,
        "Нежилая недвижимость": 20,
        "Квартира": 19,
        "Участок": 21,
        "Участок земли": 22,
    }

    rents = {
        "Коммерческая недвижимость": 16,
        "Нежилая недвижимость": 16,
        "Квартира": 12,
        "Участок": 17,
        "Участок земли": 18,
    }

    regions = {
        "Чилонзор": 24,
        "Бектемир": 25,
        "Миробод": 7,
        "Мирзо Улугбек": 20,
        "Сергели": 19,
        "Олмазор": 8,
        "Учтепа": 21,
        "Шайхонтохур": 2,
        "Юнусобод": 17,
        "Яккасарой": 22,
        "Яшнобод": 23,
    }

    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0



    
    error_counter = 0
    for order in orders:
        user_id = 1200

        if order.type == "sale":
            category_id = sales[order.property]
        elif order.type == "rent":
            category_id = rents[order.property]
        
        agency_id = 7
        try:
            region_id = regions[order.region.replace("#","")]
        except Exception as e:
            print(e)
        title = order.title
        price = order.ammount
        address = order.reference
        date = order.created_date
        content = GetContent(order)
        if str(order.user.phone) == "998935870907":
            #Майя
            user_id = 10
            counter1 += 1

            # print(f"{user_id} {category_id} {agency_id} {region_id} {title} {price} {address} {content} ")
        elif str(order.user.phone) == "998911640439":
            #Эльчин
            user_id = 11
            counter2 += 1
            # print(f"{user_id} {category_id} {agency_id} {region_id} {title} {price} {address} {content} ")
            
        elif str(order.user.phone) == "998974900737":
            #Анжелика
            user_id = 12
            counter3 += 1
        
        elif str(order.user.phone) == "998909773799":
            #Рано
            user_id = 13
            counter4 += 1
        
        elif str(order.user.phone) == "998903372426":
            #Нафиса
            user_id = 14
            counter5 += 1
        
        elif str(order.user.phone) == "998909144676":
            #Сулейман
            user_id = 15
            counter6 += 1

        if user_id!=1200:
            try:
                query = sqlalchemy.insert(myTable).values(user_id=int(user_id), category_id=int(category_id), agency_id=int(agency_id), region_id=int(region_id), title=title, price=int(price), address=address, content=content, status="moderation")
                ResultProxy = connection.execute(query)
            except Exception as e:
                print(f"Error: {e}")
                error_counter += 1

    print(f"Майя: {counter1}\nЭльчин: {counter2}\nАнжелика: {counter3}\nРано: {counter4}\nНафиса: {counter5}\nСулейман: {counter6}\n\nErrors: {error_counter}\n\nCommon: {counter1+counter2+counter3+counter4+counter5+counter6}")


def GetContent(order):
    data = []
    data.append(order.type)
    data.append(order.property)
    data.append(order.title)
    data.append(order.region)
    data.append(order.reference)
    data.append(132)
    data.append(order.room_count)
    data.append(order.square)
    data.append(order.area)
    data.append(order.state)
    data.append(order.ammount)
    data.append(order.add_info)
    data.append(order.contact)
    data.append(order.main_floor)
    data.append(order.floor)

    return GenerateEndText(data)


async def SetPhone(user, phone):
    userUpdate = api_models.TelegramUser.objects.get(telegram_id=int(user))
    userUpdate.phone = phone
    userUpdate.save()

    users = User.objects.all()
    # if users.filter(username=str(phone).replace("+","").replace(" ","").replace("-","")).count!=0:
    #     return False
    # else:

    try:
        new_user = User.objects.create_user(username=str(phone).replace("+","").replace(" ","").replace("-",""),
                                email='dightmerc@gmail.com',
                                password='helloworld8')

        comm_user = api_models.CommonRieltorUser()
        comm_user.name = new_user.username
        comm_user.user = new_user
        comm_user.rieltor = api_models.OnlineRieltor.objects.get(pk=1)
        comm_user.save()



    except Exception as e:
        print(f"\n\n{e}\n\n")

        return False
    
    
    return True

async def TickAdd(pk):
    order = api_models.Order.objects.get(pk=pk)
    order.show = order.show + 1
    order.save()
    return True

async def Search(_type, _property, price, region, room_count, area):

    order_list = api_models.Order.objects.all()

    order_list = order_list.filter(type=_type)

    if _property!="":
        order_list = order_list.filter(property=_property)
        if order_list.count()!=0:

            if price!="":
                if " " in price:
                    prices = price.split(" ")
                    order_list = order_list.filter(ammount__lte=int(prices[1]))
                    order_list = order_list.filter(ammount__gte=int(prices[0]))
                else:
                    if _type == "sale":
                        if int(price)!=200000:
                            print(f"\n\n{price}\n\n")

                            order_list = order_list.filter(ammount__lte=int(price))

                        else:

                            order_list = order_list.filter(ammount__gte=int(price))
                    elif _type == "rent":
                        if int(price)!=3500:
                            print(f"\n\n{price}\n\n")

                            order_list = order_list.filter(ammount__lte=int(price))

                        else:

                            order_list = order_list.filter(ammount__gte=int(price))
                
              

            if region!="":
                order_list = order_list.filter(region=region)

            if room_count!="":
                order_list = order_list.filter(room_count=room_count)


            if area!="":
                if " " in area:
                    areas = area.split(" ")
                    order_list = order_list.filter(area__lte=float(areas[1]))
                    order_list = order_list.filter(area__gte=float(areas[0]))
                else:
                    if int(area)!=12:
                        print(f"\n\n{area}\n\n")

                        order_list = order_list.filter(area__lte=float(area))

                    else:

                        order_list = order_list.filter(area__gte=float(area))
            
        else:
            pass


        return Paginator(order_list.filter(active=True).order_by("-id"), 2)

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
    order.type = data[0]
    order.property = data[1]
    order.title = data[2] 
    order.region = data[3]
    order.reference = data[4]
    order.location_X = data[5].split(" ")[0]
    order.location_Y = data[5].split(" ")[1]
    order.room_count = str(data[6])
    order.square = str(data[7])
    order.area = str(data[8])
    order.state = data[9]
    order.ammount = str(data[10])
    order.add_info = data[11]
    order.contact = data[12]
    order.main_floor = str(data[13])
    order.floor = str(data[14])
    order.rieltor = get_object_or_404(api_models.OnlineRieltor, name=data[15])
    order.main_state = data[16]
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
    order.type = data[0]
    order.property = data[1]
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
    order.main_floor = data[13]
    order.floor = data[14]

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
    order.type = temp.type
    order.property = temp.property
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
    order.main_floor = temp.main_floor
    order.floor = temp.floor

    order.pro_order = temp

    order.save()

    for photo in temp.photo.all():
        order.photo.add(photo)

    return order.id

async def CreateRealOnlineOrder(num):
    temp = api_models.OnlineRieltorTemporaryOrder.objects.get(pk=num)
    order = api_models.OnlineRieltorOrder()

    order.rieltor = temp.rieltor
    order.main_state = temp.main_state
    order.user = temp.user
    order.type = temp.type
    order.property = temp.property
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
    order.main_floor = temp.main_floor
    order.floor = temp.floor

    order.pro_order = temp

    order.save()

    for photo in temp.photo.all():
        order.photo.add(photo)

    return order.id
    

async def getAdmin():
    _list = []
    for user in bot_models.Admin.objects.get(pk=1).user.all():
        _list.append(user.telegram_id)
    return _list


def getMessage(number):
    return bot_models.Message.objects.get(number=number).text

def getRegions(main):
    return bot_models.Region.objects.all().filter(regionOwner=bot_models.MainRegion.objects.get(title=main).id)

def getMainRegions():
    return bot_models.MainRegion.objects.all()



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


def GenerateEndText(data):
    try:
        _type = data[0]
        _property = data[1]
        _title = data[2]
        _region = data[3]
        _reference = data[4]
        _location = data[5]
        _room_count = data[6]
        _square = data[7]
        _area = data[8]
        _state = data[9]
        _ammount = data[10]
        _add_info = data[11]
        _contact = data[12]
        _main_floor = data[13]
        _floor = data[14]

        

        first_phrase = "Продается"
        if _type == "sale":
            pass
        else:
            first_phrase = "Сдается в аренду"

        if _add_info == "None":
            _add_info = ""
        else:
            _add_info = "\n{}\n".format(_add_info)

        if _area == 0:
            _area = ""
        else:
            _area = "\nСоток: {}\n".format(_area)

        if _square == 0:
            _square = ""
        else:
            _square = "Общая площадь: {}\n кв.м".format(_square)

        data = []
        data.append(f"{first_phrase} {_property.lower()}")
        data.append(f"Район: {_region}")
        

        data.append(f"{_title}")
        

        data.append(f"Ориентир: {_reference}")

        if _property == "Участок":
            data.append(f"Комнаты: {_room_count}")
            data.append(f"Площадь: {_square} кв.м")
            if _area!="":
                data.append(_area)
            
            
            data.append(f"Цена: {_ammount} у.е")
            

            data.append(_add_info)
            

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            string = ""
            for a in data:
                string += str(a) + "\n\n"
            return(string)

            return Messages(user)['end_text_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            data.append(f"Комнаты: {_room_count}")
            if _square!="":
                data.append(_square)
            data.append(f"Этажей в доме: {_main_floor}")
            data.append(f"Этаж квартиры: {_floor}")
            
            
            data.append(f"Цена: {_ammount} у.е")
            
            data.append(_add_info)
            

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            string = ""
            for a in data:
                string += str(a) + "\n\n"
            return(string)

            return Messages(user)['end_text_flat'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            if _area!="":
                data.append(_area)
            
            
            data.append(f"Цена: {_ammount} у.е")
            
            data.append(_add_info)
            

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            string = ""
            for a in data:
                string += str(a) + "\n\n"
            return(string)

            return Messages(user)['end_text_land'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Коммерческая недвижимость":
            if _area!="":
                data.append(_area)
            if _square!="":
                data.append(_square)
            
            
            data.append(f"Цена: {_ammount} у.е")
            
            data.append(_add_info)
            

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            string = ""
            for a in data:
                string += str(a) + "\n\n"
            return(string)
            return Messages(user)['end_text_free_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
        
    except Exception as e:
        print("\n\n{}\n\n".format(e))

if __name__ == "__main__":
    TryMigrate()