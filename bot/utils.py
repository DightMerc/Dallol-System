#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.utils.helper import Helper, HelperMode, ListItem
import client
from messages import Messages



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
        _master = data[15]
        _prop_state = data[16]


        print(f"\n\n{_room_count}\n\n")
        if int(_room_count) in [1,2]:
            _room_count = f"#S{_room_count}"
        elif int(_room_count) in [3,4]:
            _room_count = f"#M{_room_count}"
        elif int(_room_count)>4:
            _room_count = f"#L{_room_count}"

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

            if _square == 0:
                _square = ""
            else:
                _square = "{}\n".format(_square)

            if _property == "Участок":
                return Messages(user)['end_text_rieltor_area'].format(_property.lower(),  _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Квартира":
                return Messages(user)['end_text_rieltor_flat'].format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Участок земли":
                return Messages(user)['end_text_rieltor_land'].format(_property.lower(), _master, first_phrase, _region, _title,_reference, _prop_state, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Коммерческая недвижимость":
                return Messages(user)['end_text_rieltor_free_area'].format(_property.lower(), _master, first_phrase, _region, _title,_reference, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
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

            if _square == 0:
                _square = ""
            else:
                _square = "{}\n".format(_square)            

            if _property == "Участок":
                _property = "Ховли"
                return Messages(user)['end_text_rieltor_area'].format(_property.capitalize(),  _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Квартира":
                return Messages(user)['end_text_rieltor_flat'].format(_property.capitalize(), _master, first_phrase, _region, _title,_reference, _prop_state, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Участок земли":
                _property = "Ер"
                return Messages(user)['end_text_rieltor_land'].format(_property.capitalize(), _master, first_phrase, _region, _title,_reference, _prop_state, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Коммерческая недвижимость":
                _property = "Уй-жойсиз қурилиш"
                return Messages(user)['end_text_rieltor_free_area'].format(_property.capitalize(), _master, first_phrase, _region, _title,_reference, _state, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
    except Exception as e:
        print("\n\n{}\n\n".format(e))




def GenerateEndText(data, mode, user):
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

        print(f"\n\n{_room_count}\n\n")

        if int(_room_count) in [1,2]:
            _room_count = f"#S{_room_count}"
        elif int(_room_count) in [3,4]:
            _room_count = f"#M{_room_count}"
        elif int(_room_count)>4:
            _room_count = f"#L{_room_count}"



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

            if _square == 0:
                _square = ""
            else:
                _square = "{}\n".format(_square)

            if _property == "Участок":
                return Messages(user)['end_text_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Квартира":
                return Messages(user)['end_text_flat'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Участок земли":
                return Messages(user)['end_text_land'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Коммерческая недвижимость":
                return Messages(user)['end_text_free_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
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

            if _square == 0:
                _square = ""
            else:
                _square = "{}\n".format(_square)

            if _property == "Участок":
                _property = "Ховли"
                return Messages(user)['end_text_area'].format(_property.capitalize(), first_phrase, _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Квартира":
                return Messages(user)['end_text_flat'].format(_property.capitalize(), first_phrase, _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Участок земли":
                _property = "Ер"
                return Messages(user)['end_text_land'].format(_property.capitalize(), first_phrase, _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
            elif _property == "Коммерческая недвижимость":
                _property = "Уй-жойсиз қурилиш"
                return Messages(user)['end_text_free_area'].format(_property.capitalize(), first_phrase, _region, _title,_reference, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
    except Exception as e:
        print("\n\n{}\n\n".format(e))

    


if __name__ == '__main__':
    print(TestStates.all())


