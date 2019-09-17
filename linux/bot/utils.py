#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.utils.helper import Helper, HelperMode, ListItem
import client


class TestStates(Helper):
    mode = HelperMode.snake_case

    STARTED = ListItem()
    LANGUAGE_SET = ListItem()

    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()

async def SearchAnnouncement(data):

    _type = data['type']
    prop = data['property']
    area = ""

    if prop!="Квартира":
        price = data['price']
        region = data['region']
        room_count = data['room_count']
        area = data['area']
        
    else:
        price = data['price']
        region = data['region']
        room_count = data['room_count']

    return await client.Search(_type, prop, price, region, room_count, area)

    
def OnlineGenerateEndText(data, user):
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
    _master = data[15]
    _prop_state = data[16]

    ann_number = client.GetLastAnnouncment()

    if client.getUserLanguage(user)=="RU":

        if _type == "sale":
            first_phrase = "Продажа"
        elif _type == "rent":
            first_phrase = "Аренда"
        else:
            first_phrase = "Поиск"


        if _add_info == "None":
            _add_info = ""
        else:
            _add_info = "\n{}\n".format(_add_info)

        if _area == 0:
            _area = ""
        else:
            _area = "Соток: {}\n".format(_area)

        if _property == "Участок":
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Ориентир: {}\n\nСостояние: {}\n\nКомнаты: {}\nПлощадь: {} кв.м\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(_property.lower(),  _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Ориентир: {}\n\nСостояние: {}\n\nКомнаты: {}\nПлощадь: {} кв.м\nЭтажей в доме: {}\nЭтаж квартиры: {}\n\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Ориентир: {}\n\nСостояние: {}\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Нежилая недвижимость":
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Ориентир: {}\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
    else:
        if _type == "sale":
            first_phrase = "Сотув"
        elif _type == "rent":
            first_phrase = "Ижара"
        else:
            first_phrase = "Кидирув"


        if _add_info == "None":
            _add_info = ""
        else:
            _add_info = "\n{}\n".format(_add_info)
        if _area == 0:
            _area = ""
        else:
            _area = "Соток: {}\n".format(_area)

        if _property == "Участок":
            _property = "Ховли"
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nҲолати: {}\n\nХоналар: {}\nУмумий майдони: {} кв.м\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(_property.lower(),  _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nnҲолати: {}\n\nХоналар: {}\nУмумий майдони: {} кв.м\nУйда каватлар: {}\nКават: {}\n\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            _property = "Ер"
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nnҲолати: {}\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Нежилая недвижимость":
            _property = "Уй-жойсиз қурилиш"
            return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nnҲолати: {}\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _state, _area, _ammount, _add_info, str(_contact).replace("+",""))



def GenerateEndText(data, mode, user):

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

    if mode:
        ann_number = data[13]
    else:
        ann_number = client.GetLastAnnouncment()

    if client.getUserLanguage(user)=="RU":


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

        if _property == "Участок":
            return "№{} {} {}\n{}\n\n{}\n🔎 Ориентир: {}\n\nКомнаты: {}\nПлощадь: {} кв.м\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            return "№{} {} {}\n{}\n\n{}\n🔎 Ориентир: {}\n\nКомнаты: {}\nПлощадь: {} кв.м\nЭтажей в доме: {}\nЭтаж квартиры: {}\n\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            return "№{} {} {}\n{}\n\n{}\n🔎 Ориентир: {}\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Нежилая недвижимость":
            return "№{} {} {}\n{}\n\n{}\n🔎 Ориентир: {}\n{}\n💵 Цена: {} у.е\n{}\n📱 Контакты: {}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
    else:

        first_phrase = "сотилади"
        if _type == "sale":
            pass
        else:
            first_phrase = "ижарага"

        if _add_info == "None":
            _add_info = ""
        else:
            _add_info = "\n{}\n".format(_add_info)

        if _area == 0:
            _area = ""
        else:
            _area = "\nСоток: {}\n".format(_area)

        if _property == "Участок":
            _property = "Ховли"
            return "№{} {} {}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nХоналар: {}\nУмумий майдони: {} кв.м\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(ann_number, _property.lower(), first_phrase, _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            return "№{} {} {}\n{}\n\n{}\n🔎 Мўлжал: {}\n\nХоналар: {}\nУмумий майдони: {} кв.м\nУйда каватлар: {}\nКават: {}\n\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(ann_number, _property.lower(), first_phrase, _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            _property = "Ер"
            return "№{} {} {}\n{}\n\n{}\n🔎 Мўлжал: {}\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(ann_number, _property.lower(), first_phrase, _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Нежилая недвижимость":
            _property = "Уй-жойсиз қурилиш"
            return "№{} {} {}\n{}\n\n{}\n🔎 Мўлжал: {}\n{}\n💵 Нарх: {} у.е\n{}\n📱 Телефон: {}".format(ann_number, _property.lower(), first_phrase, _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
    


if __name__ == '__main__':
    print(TestStates.all())


