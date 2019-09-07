from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import client


def LanguageKeyboard(user):

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('O`zbek tili'),
        KeyboardButton('Русский язык')
)

def PriceSetKeyboard(user):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('1'),
        KeyboardButton('2'),
        KeyboardButton('3'),
        KeyboardButton('4'),)
        if client.getUserLanguage(user)=="RU":
                keyboard.add(KeyboardButton('Назад'))
        else:
                keyboard.add(KeyboardButton('Оркага'))
        return keyboard

def OnlineKeyboard(user):
        online = client.getAllOnline()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for a in online:
               keyboard.add(KeyboardButton(a.name))

        if client.getUserLanguage(user)=="RU":
                keyboard.add(KeyboardButton('Назад'))
        else:
                keyboard.add(KeyboardButton('Оркага'))
        return keyboard

def OnlineKeyboardApply(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                        ).add(KeyboardButton("Сделать заказ")
                        ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                        ).add(KeyboardButton("Буюртма бериш")
                        ).add(KeyboardButton('Оркага'))
        

def MenuKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Продажа'),
                                KeyboardButton('Аренда')
                        ).add(KeyboardButton('Онлайн риелтор'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Сотув'),
                                KeyboardButton('Ижара')
                        ).add(KeyboardButton('Онлайн риелтор'))
    

def SaleAndRentKeyboard(user):
# Эълон бериш

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Подать объявление'),
                        KeyboardButton('Поиск')
                ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Эълон бериш'),
                        KeyboardButton('Қидириш')
                ).add(KeyboardButton('Оркага'))
    

def SaleSearchAndannouncementKeyboard(user):

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Участок'),
                        KeyboardButton('Квартира')
                ).row(
                        KeyboardButton('Участок земли'),
                        KeyboardButton('Нежилая недвижимость')
                ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Ховли'),
                        KeyboardButton('Квартира')
                ).row(
                        KeyboardButton('Ер'),
                        KeyboardButton('Уй-жойсиз қурилиш')
                ).add(KeyboardButton('Оркага'))

    

def OnlineSaleAndRentKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Продажа'),
                                KeyboardButton('Аренда')
                        ).add(KeyboardButton('Поиск')
                        ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Сотув'),
                                KeyboardButton('Аренда')
                        ).add(KeyboardButton('Қидириш')
                        ).add(KeyboardButton('Оркага'))
        

def EditApplyKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Изменить'),
                        KeyboardButton('Отправить')
                ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Озгартириш'),
                        KeyboardButton('Юбориш')
                ).add(KeyboardButton('Оркага'))
        

def AdminApplyKeyboard(num):
        return InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='Подтвердить',callback_data="apply {}".format(num)),
        InlineKeyboardButton(text='Удалить', callback_data="delete {}".format(num)))

def SearchKeyboard(mode, user):
        if client.getUserLanguage(user)=="RU":
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
        else:
                if mode=="Участок":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидириш'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('Назад'),
                                )
                elif mode=="Квартира":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар')).row(
                                        KeyboardButton('Қидириш'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('Назад'),
                                )
                elif mode == "Участок земли":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидириш'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('Назад'),
                                )
                elif mode == "Нежилая недвижимость":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидириш'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('Назад'),
                                )
        

def PhotoPaginationKeyboard(length, current, user):
        keyboard = InlineKeyboardMarkup()
        if current!=1:
                if current==length:
                        keyboard.row(
                                InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                                InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                                InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))
                else:
                        keyboard.row(
                                InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                                InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                                InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))
        else:
                keyboard.row(
                        InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                        InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                        InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))

        if client.getUserLanguage(user)=="RU":
                keyboard.row(InlineKeyboardButton(text="Изменить", callback_data="pagination change {}".format(current)),
                        InlineKeyboardButton(text="Удалить", callback_data="pagination delete {}".format(current)))
                keyboard.add(InlineKeyboardButton(text="Отмена", callback_data="pagination cancel"))
        else:
                keyboard.row(InlineKeyboardButton(text="Озгартириш", callback_data="pagination change {}".format(current)),
                        InlineKeyboardButton(text="Удалить", callback_data="pagination delete {}".format(current)))
                keyboard.add(InlineKeyboardButton(text="Отмена", callback_data="pagination cancel"))
        
        


        return keyboard

        

def EditOnlineMarkup(data, user):
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

        if client.getUserLanguage(user)=="RU":
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
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
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
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
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
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
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
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
        else:
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Нежилая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Даража", callback_data="edit state"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard

        

def EditMarkup(data, user):
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

        if client.getUserLanguage(user)=="RU":
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
        else:
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Нежилая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).row(
                                InlineKeyboardButton(text="Даража", callback_data="edit state"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Отмена", callback_data="edit cancel"),
                        )
                        return keyboard



def BackKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Оркага'))


def RegionKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                buttons = []
                for region in client.getRegions():
                        buttons.append(KeyboardButton("#{}".format(region.title)))
                return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('Назад')),one_time_keyboard=True, resize_keyboard=True)
        else:
                buttons = []
                for region in client.getRegions():
                        buttons.append(KeyboardButton("#{}".format(region.title)))
                return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('Оркага')),one_time_keyboard=True, resize_keyboard=True)
        


def LocationKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить геолокацию', request_location=True)).add(
                        KeyboardButton('Дальше')).add(
                        KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить геолокацию', request_location=True)).add(
                        KeyboardButton('Ўтказиб юбориш')).add(
                        KeyboardButton('Оркага'))

    

def ContactKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(
                    KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Телефон рақамингизни юбориш', request_contact=True)).add(
                    KeyboardButton('Оркага'))
    

def YesOrNoKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Продолжить')
                        ).add(
                        KeyboardButton('Отмена'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Давом еттириш')
                        ).add(
                        KeyboardButton('Бекор килиш'))
        

def RoomCountKeyboard(user):
        a= 1
        room_count = []
        while a<13:
                room_count.append(KeyboardButton(a))
                a+=1

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(keyboard=build_menu(room_count, 4, footer_buttons=KeyboardButton('Назад')),one_time_keyboard=True, resize_keyboard=True)
        else:
                return ReplyKeyboardMarkup(keyboard=build_menu(room_count, 4, footer_buttons=KeyboardButton('Оркага')),one_time_keyboard=True, resize_keyboard=True)
        


def FreeAreaKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Строится'),
                        KeyboardButton('Новое')
                ).add(KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Курилаётган'),
                        KeyboardButton('Янги')
                ).add(KeyboardButton('Назад'))
        


def BackNextKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Дальше')
                ).add(
                        KeyboardButton('Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Ўтказиб юбориш')
                ).add(
                        KeyboardButton('Оркага'))
        


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



                

    

SaleSearchAndannouncementKeyboardList = ['Участок', 'Квартира', 'Участок земли', 'Нежилая недвижимость', 'Ховли', 'Ер', 'Уй-жойсиз қурилиш']



    
    