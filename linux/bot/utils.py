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

    
def OnlineGenerateEndText(data):
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
    _master = data[13]

    ann_number = client.GetLastAnnouncment()

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

    if _property == "Участок":
        return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\nОриентир: {}\n\nКомнаты: {}\nПлощадь: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(_property.lower(),  _master, first_phrase, _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Квартира":
        return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\nОриентир: {}\n\nКомнаты: {}\nПлощадь: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _room_count, _square, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Участок земли":
        return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\nОриентир: {}\n\nПлощадь: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Нежилая недвижимость":
        return "Категория: {}\nРиелтор: {}\n\n#{}\n{}\n\n{}\nОриентир: {}\n\nСостояние: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(_property.lower(), _master, first_phrase, _region, _title,_reference, _state, _area, _ammount, _add_info, str(_contact).replace("+",""))



def GenerateEndText(data, mode):
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

    if mode:
        ann_number = data[13]
    else:
        ann_number = client.GetLastAnnouncment()


    first_phrase = "Продается"
    if _type == "sale":
        pass
    else:
        first_phrase = "Сдается в аренду"

    if _add_info == "None":
        _add_info = ""
    else:
        _add_info = "\n{}\n".format(_add_info)

    if _property == "Участок":
        return "№{} {} {}\n{}\n\n{}\nОриентир: {}\n\nКомнаты: {}\nПлощадь: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Квартира":
        return "№{} {} {}\n{}\n\n{}\nОриентир: {}\n\nКомнаты: {}\nПлощадь: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Участок земли":
        return "№{} {} {}\n{}\n\n{}\nОриентир: {}\n\nПлощадь: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
    elif _property == "Нежилая недвижимость":
        return "№{} {} {}\n{}\n\n{}\nОриентир: {}\n\nСостояние: {}\nСоток: {}\n\nЦена: {}\n{}\nКонтакты: +{}".format(ann_number, first_phrase,_property.lower(), _region, _title,_reference, _state, _area, _ammount, _add_info, str(_contact).replace("+",""))


if __name__ == '__main__':
    print(TestStates.all())


