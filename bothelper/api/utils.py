#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.utils.helper import Helper, HelperMode, ListItem

    
def OnlineGenerateEndText(data):
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
        data = []
        data.append(f"Категория: {_property.lower()}")
        data.append(f"Риелтор: {_master}")
        data.append("_ _ _")

        data.append(f"{first_phrase}")
        data.append(f"{_region}")
        data.append("_ _ _")

        data.append(f"{_title}")
        data.append(f"Ориентир: {_reference}")


        

        if _property == "Участок":
            data.append(f"Состояние: {_prop_state}")
            data.append(f"Комнаты: {_room_count}")
            data.append(f"Площадь: {_square} кв.м")
            if _area!="":
                data.append(_area)
            data.append("_ _ _")
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")

            data.append(_add_info)
            data.append("_ _ _")
            data.append(f"Контакты: {str(_contact).replace('+','')}")
            
            return data

        elif _property == "Квартира":
            data.append(f"Состояние: {_prop_state}")
            data.append(f"Комнаты: {_room_count}")
            data.append(f"Площадь: {_square} кв.м")
            data.append(f"Этажей в доме: {_main_floor}")
            data.append(f"Этаж квартиры: {_floor}")
            data.append("_ _ _")
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")

            data.append(_add_info)
            data.append("_ _ _")
            data.append(f"Контакты: {str(_contact).replace('+','')}")

            return data
        elif _property == "Участок земли":
            data.append(f"Состояние: {_prop_state}")
            if _area!="":
                data.append(_area)
            data.append("_ _ _")
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")

            data.append(_add_info)
            data.append("_ _ _")
            data.append(f"Контакты: {str(_contact).replace('+','')}")

            return data

        elif _property == "Коммерческая недвижимость":
            data.append(f"Состояние: {_prop_state}")
            if _area!="":
                data.append(_area)
            data.append("_ _ _")
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")

            data.append(_add_info)
            data.append("_ _ _")
            data.append(f"Контакты: {str(_contact).replace('+','')}")

            return data
        
    except Exception as e:
        print("\n\n{}\n\n".format(e))


if __name__ == '__main__':
    print(TestStates.all())


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
        data.append("_ _ _")

        data.append(f"{_title}")
        data.append("_ _ _")

        data.append(f"Ориентир: {_reference}")

        if _property == "Участок":
            data.append(f"Комнаты: {_room_count}")
            data.append(f"Площадь: {_square} кв.м")
            if _area!="":
                data.append(_area)
            data.append("_ _ _")
            
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")

            data.append(_add_info)
            data.append("_ _ _")

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            return(data)

            return Messages(user)['end_text_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Квартира":
            data.append(f"Комнаты: {_room_count}")
            if _square!="":
                data.append(_square)
            data.append(f"Этажей в доме: {_main_floor}")
            data.append(f"Этаж квартиры: {_floor}")
            data.append("_ _ _")
            
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")
            data.append(_add_info)
            data.append("_ _ _")

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            return(data)

            return Messages(user)['end_text_flat'].format(first_phrase,_property.lower(), _region, _title,_reference, _room_count, _square, _main_floor, _floor, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Участок земли":
            if _area!="":
                data.append(_area)
            data.append("_ _ _")
            
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")
            data.append(_add_info)
            data.append("_ _ _")

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            return(data)

            return Messages(user)['end_text_land'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _ammount, _add_info, str(_contact).replace("+",""))
        elif _property == "Коммерческая недвижимость":
            if _area!="":
                data.append(_area)
            if _square!="":
                data.append(_square)
            data.append("_ _ _")
            
            data.append(f"Цена: {_ammount} у.е")
            data.append("_ _ _")
            data.append(_add_info)
            data.append("_ _ _")

            data.append(f"Контакты: {str(_contact).replace('+','')}")
            return(data)
            return Messages(user)['end_text_free_area'].format(first_phrase,_property.lower(), _region, _title,_reference, _area, _square, _ammount, _add_info, str(_contact).replace("+",""))
        
    except Exception as e:
        print("\n\n{}\n\n".format(e))

