#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import TestStates
import client



help_message = 'Для того, чтобы изменить текущее состояние пользователя, ' \
               f'отправь команду "/setstate x", где x - число от 0 до {len(TestStates.all()) - 1}.\n' \
               'Чтобы сбросить текущее состояние, отправь "/setstate" без аргументов.'

start_message = 'Привет! Это демонстрация работы FSM.\n' + help_message
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_change_success_message = 'Текущее состояние успешно изменено'
state_reset_message = 'Состояние успешно сброшено'
current_state_message = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'




def Messages(user):

    if client.getUserLanguage(user)=="RU":
    
        MESSAGES = {
            'start': client.getMessage(1).text,
            
            'language': client.getMessage(2).text,

            'area': client.getMessage(3).text,
            'flat': client.getMessage(4).text,
            'land': client.getMessage(5).text,
            'free_area': client.getMessage(6).text,

            'title_added': client.getMessage(7).text,

            'region_added': client.getMessage(8).text,

            'geo1': client.getMessage(9).text,
            'geo2': client.getMessage(10).text,
            'geo3': client.getMessage(11).text,

            'area_started': client.getMessage(12).text,
            'flat_started': client.getMessage(13).text,
            'land_started': client.getMessage(14).text,
            'free_area_started': client.getMessage(15).text,

            'area_rooms_added': client.getMessage(16).text,
            'area_square_added': client.getMessage(17).text,
            
            'flat_rooms_added': client.getMessage(16).text,
            'flat_square_added': client.getMessage(17).text,

            'land_square_added': client.getMessage(17).text,

            'free_area_square_added': client.getMessage(17).text,
            'free_area_state_added': client.getMessage(14).text,

            'photo1': client.getMessage(18).text,
            'photo2': client.getMessage(19).text,
            'photo3': client.getMessage(20).text,

            'ammount': client.getMessage(21).text,
            'ammount_set': client.getMessage(22).text,

            'contacts': client.getMessage(23).text,

            'price_list': client.getMessage(24).text,

            'choose_action': client.getMessage(25).text,
            'filter': client.getMessage(26).text,
            'send_text': client.getMessage(27).text,

            'choose_photo_edit': client.getMessage(28).text,

            'edit_text_now': client.getMessage(29).text,

            'data_clear': client.getMessage(30).text,

            "digits_only": client.getMessage(61).text,

            "price_list2": client.getMessage(63).text,

            


        }
    else:
        MESSAGES = {
            'start': client.getMessage(31).text,
            
            'language': client.getMessage(32).text,

            'area': client.getMessage(33).text,
            'flat': client.getMessage(34).text,
            'land': client.getMessage(35).text,
            'free_area': client.getMessage(36).text,

            'title_added': client.getMessage(37).text,

            'region_added': client.getMessage(38).text,

            'geo1': client.getMessage(39).text,
            'geo2': client.getMessage(40).text,
            'geo3': client.getMessage(41).text,

            'area_started': client.getMessage(42).text,
            'flat_started': client.getMessage(43).text,
            'land_started': client.getMessage(44).text,
            'free_area_started': client.getMessage(45).text,

            'area_rooms_added': client.getMessage(46).text,
            'area_square_added': client.getMessage(47).text,
            
            'flat_rooms_added': client.getMessage(46).text,
            'flat_square_added': client.getMessage(47).text,

            'land_square_added': client.getMessage(47).text,

            'free_area_square_added': client.getMessage(47).text,
            'free_area_state_added': client.getMessage(44).text,

            'photo1': client.getMessage(48).text,
            'photo2': client.getMessage(49).text,
            'photo3': client.getMessage(50).text,

            'ammount': client.getMessage(51).text,
            'ammount_set': client.getMessage(52).text,

            'contacts': client.getMessage(53).text,

            'price_list': client.getMessage(54).text,
            'choose_action': client.getMessage(55).text,
            'filter': client.getMessage(56).text,
            'send_text': client.getMessage(57).text,

            'choose_photo_edit': client.getMessage(58).text,

            'edit_text_now': client.getMessage(59).text,

            'data_clear': client.getMessage(60).text,

            "digits_only": client.getMessage(62).text,

            "price_list2": client.getMessage(64).text,





        }

    return MESSAGES


