from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import client

def LanguageKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('O`zbek tili'),
        KeyboardButton('Русский язык')
)

def PriceSetKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('1'),
        KeyboardButton('2'),
        KeyboardButton('3'),
        KeyboardButton('4'),
).add(KeyboardButton('Назад'))

def OnlineKeyboard():
        online = client.getAllOnline()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for a in online:
               keyboard.add(KeyboardButton(a.name))
        return keyboard.add(KeyboardButton('Назад'))

def OnlineKeyboardApply():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
        ).add(KeyboardButton("Сделать заказ")
        ).add(KeyboardButton('Назад'))

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

def OnlineSaleAndRentKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                KeyboardButton('Продажа'),
                KeyboardButton('Аренда')
        ).add(KeyboardButton('Поиск')
        ).add(KeyboardButton('Назад'))

def EditApplyKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Изменить'),
        KeyboardButton('Отправить')
).add(KeyboardButton('Назад'))

def AdminApplyKeyboard(num):
        return InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='Подтвердить',callback_data="apply {}".format(num)),
        InlineKeyboardButton(text='Удалить', callback_data="delete {}".format(num)))

def SearchKeyboard(mode):
        if mode=="Участок":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Цена'),
                        KeyboardButton('Район'),
                        KeyboardButton('Комнаты'),
                        KeyboardButton('Сотки')).row(
                                KeyboardButton('Поиск'),
                                KeyboardButton('Очистить'),

                        ).add(
                                KeyboardButton('Назад'),
                        )
        elif mode=="Квартира":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Цена'),
                        KeyboardButton('Район'),
                        KeyboardButton('Комнаты')).row(
                                KeyboardButton('Поиск'),
                                KeyboardButton('Очистить'),

                        ).add(
                                KeyboardButton('Назад'),
                        )
        elif mode == "Участок земли":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Цена'),
                        KeyboardButton('Район'),
                        KeyboardButton('Комнаты'),
                        KeyboardButton('Сотки')).row(
                                KeyboardButton('Поиск'),
                                KeyboardButton('Очистить'),

                        ).add(
                                KeyboardButton('Назад'),
                        )
        elif mode == "Нежилая недвижимость":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Цена'),
                        KeyboardButton('Район'),
                        KeyboardButton('Комнаты'),
                        KeyboardButton('Сотки')).row(
                                KeyboardButton('Поиск'),
                                KeyboardButton('Очистить'),

                        ).add(
                                KeyboardButton('Назад'),
                        )
        


def EditMarkup(data):
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

        keyboard = InlineKeyboardMarkup()

        if _property == "Участок":
                keyboard.add(
                        InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                ).row(
                        InlineKeyboardButton(text="Описание", callback_data="edit title"),
                        InlineKeyboardButton(text="Район", callback_data="edit region")
                ).row(
                        InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                        InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                ).add(
                        InlineKeyboardButton(text="Локация", callback_data="edit location")
                ).row(
                        InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                        InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                ).row(
                        InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                        InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                ).add(
                        InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                ).add(
                        InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                )
                return keyboard

        elif _property == "Квартира":
                keyboard.add(
                        InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                ).row(
                        InlineKeyboardButton(text="Описание", callback_data="edit title"),
                        InlineKeyboardButton(text="Район", callback_data="edit region")
                ).row(
                        InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                        InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                ).add(
                        InlineKeyboardButton(text="Локация", callback_data="edit location")
                ).add(
                        InlineKeyboardButton(text="Площадь", callback_data="edit square")
                ).row(
                        InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                        InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                ).add(
                        InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                ).add(
                        InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                )
                return keyboard
        elif _property == "Участок земли":
                keyboard.add(
                        InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                ).row(
                        InlineKeyboardButton(text="Описание", callback_data="edit title"),
                        InlineKeyboardButton(text="Район", callback_data="edit region")
                ).add(
                        InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                ).add(
                        InlineKeyboardButton(text="Локация", callback_data="edit location")
                ).row(
                        InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                        InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                ).row(
                        InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                        InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                ).add(
                        InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                ).add(
                        InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                )
                return keyboard
        elif _property == "Нежилая недвижимость":
                keyboard.add(
                        InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                ).row(
                        InlineKeyboardButton(text="Описание", callback_data="edit title"),
                        InlineKeyboardButton(text="Район", callback_data="edit region")
                ).add(
                        InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                ).add(
                        InlineKeyboardButton(text="Локация", callback_data="edit location")
                ).row(
                        InlineKeyboardButton(text="Состояние", callback_data="edit state"),
                        InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                ).row(
                        InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                        InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                ).add(
                        InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                ).add(
                        InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                )
                return keyboard



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

def ContactKeyboard():

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(
                    KeyboardButton('Назад'))

def YesOrNoKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                KeyboardButton('Продолжить')
                ).add(
                    KeyboardButton('Отмена'))

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


def BackNextKeyboard():
        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                KeyboardButton('Дальше')
        ).add(
                KeyboardButton('Назад')
                        )


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


    
    