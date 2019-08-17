from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import client

def LanguageKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('O`zbek tili'),
        KeyboardButton('Русский язык')
)

def MenuKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Продажа'),
        KeyboardButton('Аренда')
).add(KeyboardButton('Онлайн риелтор'))

def SaleAndRentKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Подать объявление'),
        KeyboardButton('Поиск')
).add(KeyboardButton('Назад'))

def SaleSearchAndannouncementKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Участок'),
        KeyboardButton('Квартира')
).row(
        KeyboardButton('Участок земли'),
        KeyboardButton('Нежилая недвижимость')
).add(KeyboardButton('Назад'))


def BackKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Назад'))


def RegionKeyboard():
        buttons = []
        for region in client.getRegions():
                buttons.append(KeyboardButton("#{}".format(region.title)))
        return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('Назад')),one_time_keyboard=True, resize_keyboard=True)


def LocationKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить геолокацию', request_location=True)).add(
            KeyboardButton('Дальше')).add(
                    KeyboardButton('Назад'))

def RoomCountKeyboard():
        a= 1
        room_count = []
        while a<13:
                room_count.append(KeyboardButton(a))
                a+=1
        return ReplyKeyboardMarkup(keyboard=build_menu(room_count, 4, footer_buttons=KeyboardButton('Назад')),one_time_keyboard=True, resize_keyboard=True)


def FreeAreaKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Строится'),
        KeyboardButton('Новое')
).add(KeyboardButton('Назад'))


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu



                

    

SaleSearchAndannouncementKeyboardList = ['Участок', 'Квартира', 'Участок земли', 'Нежилая недвижимость']


    
    