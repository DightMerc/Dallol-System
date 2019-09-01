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


def Messages():
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









        



        'current_state': current_state_message,
    }

    return MESSAGES


