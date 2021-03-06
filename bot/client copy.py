import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from utils import TestStates, GenerateEndText, SearchAnnouncement, OnlineGenerateEndText
from messages import Messages

from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, InputFile

import client

import keyboards
from typing import Optional
import os
import aioredis



logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                     level=logging.DEBUG)



bot = Bot(token="796303915:AAF4MJs2lqEYxUWtK-7VSjYVWGjeLhNEXnU")
storage = RedisStorage2(db=6)
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())





# States
class User(StatesGroup):
    started = State() 
    language_set = State() 
    photo = State()
    ammount_set = State()
    add_info = State()
    contact = State()
    edit = State()

class Admin(StatesGroup):
    started = State() 

class Search(StatesGroup):
    started = State() 
    price = State()
    region = State()
    room_count = State()
    area = State()

    set = State()

class Edit(StatesGroup):
    started = State()
    second = State()
    property = State()
    photo = State()
    photoNew = State()

class Sale(StatesGroup):
    started = State()
    announcement = State()
    search = State()
    type_choosen = State()
    title_added = State()
    region_added = State()
    reference = State()
    location_True_or_False = State()


class OnlineSearch(StatesGroup):
    started = State()
    announcement = State()
    search = State()
    type_choosen = State()
    title_added = State()
    region_added = State()
    reference = State()
    location_True_or_False = State()

class Area(StatesGroup):
    started = State()
    square = State()
    area = State()
    

class Flat(StatesGroup):
    started = State()
    square = State()
    area = State()

class Land(StatesGroup):
    started = State()
    square = State()
    area = State()

class Free_area(StatesGroup):
    started = State()
    square = State()
    state = State()

class Rent(StatesGroup):
    started = State()
    announcement = State()
    search = State()
    type_choosen = State()
    title_added = State()
    region_added = State()
    reference = State()
    location_True_or_False = State()

class Online(StatesGroup):
    started = State()
    mode = State()
    order = State()




@dp.message_handler(commands=['start'], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    user = message.from_user.id


    if not os.path.exists(os.getcwd()+"/Users/" + str(user)):
        os.mkdir(os.getcwd()+"/Users/" + str(user), 0o777)

    if not client.userExsists(user):
        client.userCreate(message.from_user)

    await state.set_data({})
    
    await User.started.set()
    
    await bot.send_chat_action(user, action="typing")

    await bot.send_message(user, Messages()['start'].format(message.from_user.first_name))
    await bot.send_message(user, Messages()['language'], reply_markup=keyboards.LanguageKeyboard())

@dp.message_handler(commands=['state'], state="*")
async def get_MyState(message: types.Message):
    user = message.from_user.id

    state = await dp.current_state(user=message.from_user.id).get_state()

    await bot.send_message(user, state)

@dp.message_handler(text="Назад", state="*")
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    current_state = await dp.current_state(user=message.from_user.id).get_state()

    if current_state in ["Sale:started", "Rent:started"]:

        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Sale:announcement":

        await Sale.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    
    elif current_state == "Sale:type_choosen":

        await Sale.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif current_state in "Rent:announcement":

        await Rent.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Rent:type_choosen":

        await Rent.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state in ["Rent:title_added", "Rent:region_added", "Rent:reference", "Rent:OnlineSearch.","Sale:title_added", "Sale:region_added", "Sale:reference", "Sale:OnlineSearch"]:

        if "Rent" in current_state:
            await Rent.announcement.set()
        elif "Sale" in current_state:
            await Sale.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif "Area" in current_state:
        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif "Flat" in current_state:
        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif "Land" in current_state:
        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif "Free_area" in current_state:
        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif current_state == "Search:started":
        await Sale.search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Online:order":
        await Online.mode.set()

        text = "Выберите действие"
        markup = keyboards.OnlineKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Online:mode":
        await Online.started.set()

        text = "Выберите действие"
        markup = keyboards.OnlineSaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Online:started":
        await User.language_set.set()

        await state.set_data({})


        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "User:edit":
        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        await state.set_data({})


        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    
    elif current_state in ["Search:price", "Search:region", "Search:room_count", "Search:area"]:
        
        async with state.proxy() as data:
            prop = data['property']

        await Search.started.set()

        text = "Установите фильтр"
        markup = keyboards.SearchKeyboard(prop)
        await bot.send_message(user, text, reply_markup=markup)

    elif current_state == "Sale:search":
        await Sale.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    
    elif current_state == "Rent:search":
        await Rent.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

        



@dp.message_handler(state=User.ammount_set)
async def user_ammount_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await User.add_info.set()
    async with state.proxy() as data:
        data['ammount'] = recieved_text

    text = Messages()["ammount_set"]
    markup = keyboards.BackNextKeyboard()

    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=User.add_info)
async def user_info_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    if not recieved_text in ["Дальше"]:

        await User.contact.set()
        async with state.proxy() as data:
            data['add_info'] = recieved_text

        text = Messages()["contacts"]
        markup = keyboards.ContactKeyboard()

        await bot.send_message(user, text, reply_markup=markup)
    else:

        text = Messages()["contacts"]
        await User.contact.set()
        async with state.proxy() as data:
            data['add_info'] = "None"

        markup = keyboards.ContactKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=User.contact, content_types=types.ContentType.CONTACT)
async def user_contact_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id

    phone = message.contact.phone_number


    async with state.proxy() as data:
        data['phone'] = phone

    async with state.proxy() as data:

        _type = data['type']
        
        _property = data['property']
        _title = data['{} title'.format(_type)]
        _region = data['{} region'.format(_type)]
        _reference = data['{} reference'.format(_type)]
        _location = data['{} location'.format(_type)]
        try:
            _room_count = data['{} room_count'.format(_type)]
        except Exception as e:
            _room_count = 0

        try:
            _square = data['{} square'.format(_type)]
        except Exception as e:
            _square = 0

        
        
        try:
            _area = data['{} area'.format(_type)]
        except Exception as e:
            _area = 0
        
        try:
            _state = data['{} state'.format(_type)]
        except Exception as e:
            _state = ""

        _ammount = data['ammount']
        _add_info = data['add_info']
        _contact = data['phone']



        user_data = []
        user_data.append(_type)
        user_data.append(_property)
        user_data.append(_title)
        user_data.append(_region)
        user_data.append(_reference)
        user_data.append(_location)
        user_data.append(_room_count)
        user_data.append(_square)
        user_data.append(_area)
        user_data.append(_state)
        user_data.append(_ammount)
        user_data.append(_add_info)
        user_data.append(_contact)

        try:
            _online_status = data["online"]
            user_data.append(data['master'])

            text = OnlineGenerateEndText(user_data)
        except Exception as e:
            text = GenerateEndText(user_data, False)


    await User.edit.set()

    if _location != "0 0":
        X = _location.split(" ")[0]
        Y = _location.split(" ")[1]
        await bot.send_chat_action(user, action="find_location")

        await bot.send_location(user, latitude=X, longitude=Y)

    photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
    media = []
    for photo in photoes:
        media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
    

    markup = keyboards.EditApplyKeyboard()
    if len(media)!=1:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_media_group(user, media)
    else:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
    await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=User.edit)
async def user_edit_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id
    recieved_text = message.text

    if recieved_text == "Изменить":
        await Edit.started.set()

        async with state.proxy() as data:

            _type = data['type']
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]

            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)



            try:
                _online_status = data["online"]
                user_data.append(data['master'])

                text = OnlineGenerateEndText(user_data)

                if _location != "0 0":
                    X = _location.split(" ")[0]
                    Y = _location.split(" ")[1]
                    await bot.send_chat_action(user, action="find_location")

                    await bot.send_location(user, latitude=X, longitude=Y)

                photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
                media = []
                for photo in photoes:
                    media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

                if len(media)!=1:
                    await bot.send_chat_action(user, action="upload_photo")
                    await bot.send_media_group(user, media)
                else:
                    await bot.send_chat_action(user, action="upload_photo")
                    await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))

                markup = keyboards.EditOnlineMarkup(user_data)
                
                await bot.send_message(user, text, reply_markup=markup)

            except Exception as e:
                text = GenerateEndText(user_data, False)

                if _location != "0 0":
                    X = _location.split(" ")[0]
                    Y = _location.split(" ")[1]
                    await bot.send_chat_action(user, action="find_location")

                    await bot.send_location(user, latitude=X, longitude=Y)

                photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
                media = []
                for photo in photoes:
                    media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

                if len(media)!=1:
                    await bot.send_chat_action(user, action="upload_photo")
                    await bot.send_media_group(user, media)
                else:
                    await bot.send_chat_action(user, action="upload_photo")
                    await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))

                markup = keyboards.EditMarkup(user_data)
                
                await bot.send_message(user, text, reply_markup=markup)

    elif recieved_text == "Отправить":

        await User.language_set.set()

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

        async with state.proxy() as data:

            _type = data['type']
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]

            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)



            try:
                _online_status = data["online"]
                user_data.append(data['master'])

                text = OnlineGenerateEndText(user_data)

                
                media = []
                photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
                for photo in photoes:
                    media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
                #заменить user на admin
                admin = await client.getAdmin()

                if _location != "0 0":
                    X = _location.split(" ")[0]
                    Y = _location.split(" ")[1]
                    await bot.send_chat_action(user, action="find_location")

                    await bot.send_location(admin[0], latitude=X, longitude=Y)

                
                if len(media)!=1:
                    await bot.send_chat_action(user, action="upload_photo")

                    await bot.send_media_group(admin[0], media)
                else:
                    await bot.send_chat_action(user, action="upload_photo")

                    await bot.send_photo(admin[0], InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
                    
                num = client.createOnlineTemporaryOrder(user, user_data)

                markup = keyboards.AdminApplyKeyboard(num)

                await bot.send_message(admin[0], text, reply_markup=markup)

            except Exception as e:
                text = GenerateEndText(user_data, False)

                
                media = []
                photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
                for photo in photoes:
                    media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
                #заменить user на admin
                admin = await client.getAdmin()

                if _location != "0 0":
                    X = _location.split(" ")[0]
                    Y = _location.split(" ")[1]
                    await bot.send_chat_action(user, action="find_location")

                    await bot.send_location(admin[0], latitude=X, longitude=Y)

                if len(media)!=1:
                    await bot.send_chat_action(user, action="upload_photo")

                    await bot.send_media_group(admin[0], media)
                else:
                    await bot.send_chat_action(user, action="upload_photo")
                    with open(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]) as f:
                        photo = inputFile(f)
                    await bot.send_photo(admin[0], photo)

                num = client.createTemporaryOrder(user, user_data)


                markup = keyboards.AdminApplyKeyboard(num)

                await bot.send_message(admin[0], text, reply_markup=markup)

@dp.callback_query_handler(state=Admin.started)
async def callback_edit_message_handler(callback_query: types.CallbackQuery, state: FSMContext):   
    user = callback_query.from_user.id
    data = callback_query.data

    if "delete" in data:
        num = int(data.replace("delete ", ""))

        markup=None
        text = "Объявление удалено"

        await bot.answer_callback_query(callback_query.id, text=text)

        await bot.delete_message(user, callback_query.message.message_id)
        
    elif "apply":
        num = int(data.replace("apply ", ""))

        await client.CreateRealOrder(num)

        await bot.edit_message_reply_markup(user, callback_query.message.message_id, reply_markup=None)
        text = "Объявление опубликовано"
        await bot.answer_callback_query(callback_query.id, text=text)


@dp.callback_query_handler(state=Edit.photo)
async def callback_pagination_handler(callback_query: types.CallbackQuery, state: FSMContext):   
    user = callback_query.from_user.id
    data = callback_query.data
    
    content = data.replace("pagination", "")


    if "next" in content:

        await bot.answer_callback_query(callback_query.id)


        async with state.proxy() as data:
            message_id = data['last']

        number = int(content.replace("next ", ""))

        path = os.getcwd()+"/Users/"+"{}/".format(user)
        photoes = os.listdir(path)

        if number!=len(photoes)+1:
            number = number
        else:
            number = 1

        markup = keyboards.PhotoPaginationKeyboard(len(photoes), number)
        text = "Выберите фото, которое хотите изменить"
        media = InputFile(path + photoes[number-1])

        
        await bot.edit_message_media(media=types.input_media.InputMediaPhoto(media=media), chat_id=user, message_id=message_id, reply_markup=markup)
        

    if "prev" in content:

        await bot.answer_callback_query(callback_query.id)


        async with state.proxy() as data:
            message_id = data['last']

        number = int(content.replace("prev ", ""))

        path = os.getcwd()+"/Users/"+"{}/".format(user)
        photoes = os.listdir(path)

        if number!=0:
            number = number
        else:
            number = len(photoes)

        markup = keyboards.PhotoPaginationKeyboard(len(photoes), number)
        text = "Выберите фото, которое хотите изменить"
        media = InputFile(path + photoes[number-1])

        await bot.edit_message_media(media=types.input_media.InputMediaPhoto(media=media), chat_id=user, message_id=message_id, reply_markup=markup)

    if "delete" in content:
        
        await bot.answer_callback_query(callback_query.id)

        async with state.proxy() as data:
            message_id = data['last']

        number = int(content.replace("delete ", ""))

        path = os.getcwd()+"/Users/"+"{}/".format(user)
        photoes = os.listdir(path)
        os.remove(path + photoes[number - 1])

        photoes = os.listdir(path)

        if len(photoes)!=0:
            if number!=1:
                markup = keyboards.PhotoPaginationKeyboard(len(photoes), number - 1)
                media = InputFile(path + photoes[number-2])
            else:
                markup = keyboards.PhotoPaginationKeyboard(len(photoes), number)
                media = InputFile(path + photoes[0])



            await bot.edit_message_media(media=types.input_media.InputMediaPhoto(media=media), chat_id=user, message_id=message_id, reply_markup=markup)


        else:
            await bot.delete_message(user, message_id)

            await Edit.photoNew.set()

            text = Messages()["photo1"]
            await bot.send_message(user, text, reply_markup=None)

            text = Messages()["photo2"]
            markup = keyboards.BackKeyboard()
            await bot.send_message(user, text, reply_markup=markup)
        
    if 'cancel' in content:
        await bot.answer_callback_query(callback_query.id)

        async with state.proxy() as data:
            message_id = data['last']

            await bot.delete_message(user, message_id)

            _type = data['type']
            
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]
            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0

            
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)

            try:
                _online_status = data["online"]
                user_data.append(data['master'])

                text = OnlineGenerateEndText(user_data)
            except Exception as e:
                text = GenerateEndText(user_data, False)


        await User.edit.set()

        if _location != "0 0":
            X = _location.split(" ")[0]
            Y = _location.split(" ")[1]
            await bot.send_chat_action(user, action="find_location")

            await bot.send_location(user, latitude=X, longitude=Y)

        photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
        media = []
        for photo in photoes:
            media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
        

        markup = keyboards.EditApplyKeyboard()
        if len(media)!=1:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_media_group(user, media)
        else:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
        await bot.send_message(user, text, reply_markup=markup)
    
    if "change" in content:
        number = int(content.replace("change ", ""))

        async with state.proxy() as data:
            message_id = data['last']

        await bot.delete_message(user, message_id)

        path = os.getcwd()+"/Users/"+"{}/".format(user)
        photoes = os.listdir(path)
        os.remove(path + photoes[number - 1])

        await Edit.photoNew.set()

        text = Messages()["photo1"]
        await bot.send_message(user, text, reply_markup=None)

        text = Messages()["photo2"]
        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=Edit.photoNew, content_types=types.ContentType.PHOTO)
async def sale_edit_photo_added_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id

    count = len(os.listdir(os.getcwd()+"/Users/" + str(user)+"/"))

    if count+1<10:
        text = Messages()["photo3"].format(count+1)

        photo = await bot.get_file(message.photo[-1].file_id)
        await photo.download(os.getcwd()+"/Users/" + str(user)+"/{}.jpg".format(message.photo[-1].file_id))

        markup = keyboards.BackNextKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    

@dp.callback_query_handler(state=Edit.started)
async def callback_edit_handler(callback_query: types.CallbackQuery, state: FSMContext):   
    user = callback_query.from_user.id
    data = callback_query.data

    content = data.replace("edit ","")
    if not content=="cancel":
    
        async with state.proxy() as data:
            _type = data["type"]
            try:
                if content!="photo":
                    field = data["{} {}".format(_type, content)]
                else:
                    field = ""

                data["edit"] = "{} {}".format(_type, content)

            except Exception as e:
                if content!="photo":
                    field = data["{}".format(content)]
                else:
                    field = ""

                data["edit"] = "{}".format(content)


        await Edit.second.set()
        
        markup = None
        text = "Сейчас: {}\n\nОтправьте новый текст".format(field)

        if content == "property":
            markup = keyboards.YesOrNoKeyboard()
            text = "Данные будут потеряны. Продолжить?"
            await Edit.property.set()
        elif content == "region":
            markup = keyboards.RegionKeyboard()
            text = Messages()["title_added"]
        elif content == "state":
            markup = keyboards.FreeAreaKeyboard()
            text = Messages()["free_area_started"]
        elif content == "location":
            text = Messages()["geo1"]
            await bot.send_message(user, text)

            text = Messages()["geo2"]
            await bot.send_message(user, text)

            text = Messages()["geo3"]
            markup = keyboards.LocationKeyboard()
        elif content == "master":
            markup = keyboards.OnlineKeyboard()
            text = "Сейчас: {}\n\nВыберите другой вариант".format(field)
        elif content == "photo":
            path = os.getcwd()+"/Users/"+"{}/".format(user)

            await Edit.photo.set()


            photoes = os.listdir(path)
            markup = keyboards.PhotoPaginationKeyboard(len(photoes), 1)
            text = "Выберите фото, которое хотите изменить"
            media = InputFile(path + photoes[0])
            await bot.send_chat_action(user, action="upload_photo")
            message = await bot.send_photo(user, media, reply_markup=markup)

            await bot.send_message(user, text, reply_markup=None)


            async with state.proxy() as data:
                data['last'] = message.message_id

            return

            


        await bot.send_message(user, text, reply_markup=markup)
    else:
        async with state.proxy() as data:

            _type = data['type']
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]
            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0

            
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)

            try:
                _online_status = data["online"]
                user_data.append(data['master'])

                text = OnlineGenerateEndText(user_data)
            except Exception as e:
                text = GenerateEndText(user_data, False)

        await User.edit.set()
        if _location != "0 0":
            X = _location.split(" ")[0]
            Y = _location.split(" ")[1]
            await bot.send_chat_action(user, action="find_location")

            await bot.send_location(user, latitude=X, longitude=Y)

        photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
        media = []
        for photo in photoes:
            media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

        markup = keyboards.EditApplyKeyboard()
        if len(media)!=1:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_media_group(user, media)
        else:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
        await bot.send_message(user, text, reply_markup=markup)

    




@dp.message_handler(state=Edit.second)
async def text_edit_handler(message: types.Message, state: FSMContext):   
    user = message.from_user.id
    recieved_text = message.text
    
    async with state.proxy() as data:
        data[data["edit"]] = recieved_text

    async with state.proxy() as data:

        _type = data['type']
        _property = data['property']
        _title = data['{} title'.format(_type)]
        _region = data['{} region'.format(_type)]
        _reference = data['{} reference'.format(_type)]
        _location = data['{} location'.format(_type)]

        try:
            _room_count = data['{} room_count'.format(_type)]
        except Exception as e:
            _room_count = 0

        try:
            _square = data['{} square'.format(_type)]
        except Exception as e:
            _square = 0
        
        try:
            _area = data['{} area'.format(_type)]
        except Exception as e:
            _area = 0
        
        try:
            _state = data['{} state'.format(_type)]
        except Exception as e:
            _state = ""

        _ammount = data['ammount']
        _add_info = data['add_info']
        _contact = data['phone']



        user_data = []
        user_data.append(_type)
        user_data.append(_property)
        user_data.append(_title)
        user_data.append(_region)
        user_data.append(_reference)
        user_data.append(_location)
        user_data.append(_room_count)
        user_data.append(_square)
        user_data.append(_area)
        user_data.append(_state)
        user_data.append(_ammount)
        user_data.append(_add_info)
        user_data.append(_contact)


        try:
            _online_status = data["online"]
            user_data.append(data['master'])

            text = OnlineGenerateEndText(user_data)
            markup = keyboards.EditOnlineMarkup(user_data)

        except Exception as e:
            text = GenerateEndText(user_data, False)
            markup = keyboards.EditMarkup(user_data)


    if _location != "0 0":
        X = _location.split(" ")[0]
        Y = _location.split(" ")[1]
        await bot.send_chat_action(user, action="find_location")

        await bot.send_location(user, latitude=X, longitude=Y)
    
    photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
    media = []
    for photo in photoes:
        media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

    if len(media)!=1:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_media_group(user, media)
    else:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
   

    await Edit.started.set()
    
    await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=Edit.second, content_types=types.ContentType.LOCATION)
async def location_edit_handler(message: types.Message, state: FSMContext):   
    user = message.from_user.id
    
    async with state.proxy() as data:
        data[data["edit"]] = "{} {}".format(message.location.latitude, message.location.longitude)
    
    async with state.proxy() as data:

        _type = data['type']
        _property = data['property']
        _title = data['{} title'.format(_type)]
        _region = data['{} region'.format(_type)]
        _reference = data['{} reference'.format(_type)]
        _location = data['{} location'.format(_type)]

        try:
            _room_count = data['{} room_count'.format(_type)]
        except Exception as e:
            _room_count = 0

        try:
            _square = data['{} square'.format(_type)]
        except Exception as e:
            _square = 0
        
        try:
            _area = data['{} area'.format(_type)]
        except Exception as e:
            _area = 0
        
        try:
            _state = data['{} state'.format(_type)]
        except Exception as e:
            _state = ""

        _ammount = data['ammount']
        _add_info = data['add_info']
        _contact = data['phone']



        user_data = []
        user_data.append(_type)
        user_data.append(_property)
        user_data.append(_title)
        user_data.append(_region)
        user_data.append(_reference)
        user_data.append(_location)
        user_data.append(_room_count)
        user_data.append(_square)
        user_data.append(_area)
        user_data.append(_state)
        user_data.append(_ammount)
        user_data.append(_add_info)
        user_data.append(_contact)


        text = GenerateEndText(user_data, False)

    if _location != "0 0":
        X = _location.split(" ")[0]
        Y = _location.split(" ")[1]

        await bot.send_chat_action(user, action="find_location")
        await bot.send_location(user, latitude=X, longitude=Y)

    photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
    media = []
    for photo in photoes:
        media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

    if len(media)!=1:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_media_group(user, media)
    else:
        await bot.send_chat_action(user, action="upload_photo")
        await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
   
    markup = keyboards.EditMarkup(user_data)

    await Edit.started.set()
    
    await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=Edit.property)
async def edit_property_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text == "Продолжить":
        await Sale.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    else:
        user = message.from_user.id
        await Edit.started.set()

        async with state.proxy() as data:

            _type = data['type']
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]

            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)



            text = GenerateEndText(user_data, False)

        if _location != "0 0":
            X = _location.split(" ")[0]
            Y = _location.split(" ")[1]
            await bot.send_chat_action(user, action="find_location")

            await bot.send_location(user, latitude=X, longitude=Y)

        photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
        media = []
        for photo in photoes:
            media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))

        if len(media)!=1:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_media_group(user, media)
        else:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))

        markup = keyboards.EditMarkup(user_data)
        
        await bot.send_message(user, text, reply_markup=markup)



    

    
            
        

@dp.message_handler(text="Дальше", state="*")
async def next_button_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    my_state = await dp.current_state(user=message.from_user.id).get_state()

    if my_state in "Rent:reference":
        user = message.from_user.id
        recieved_text = message.text

        await Rent.location_True_or_False.set()

        async with state.proxy() as data:
            data["rent location"] = "0 0"

            _type = data['property']

        if _type == "Участок":
            await Area.started.set()
            text = Messages()["area_started"]
            markup = keyboards.RoomCountKeyboard()

        if _type == "Квартира":
            await Flat.started.set()
            text = Messages()["flat_started"]
            markup = keyboards.RoomCountKeyboard()

        if _type == "Участок земли":
            await Land.started.set()
            text = Messages()["land_started"]
            markup = keyboards.BackKeyboard()

        if _type == "Нежилая недвижимость":
            await Free_area.started.set()
            text = Messages()["free_area_started"]
            markup = keyboards.FreeAreaKeyboard()


        await bot.send_message(user, text, reply_markup=markup)
    elif my_state in "Sale:reference":
        user = message.from_user.id
        recieved_text = message.text

        await Sale.location_True_or_False.set()

        async with state.proxy() as data:
            data["sale location"] = "0 0"

            _type = data['property']

        if _type == "Участок":
            await Area.started.set()
            text = Messages()["area_started"]
            markup = keyboards.RoomCountKeyboard()

        if _type == "Квартира":
            await Flat.started.set()
            text = Messages()["flat_started"]
            markup = keyboards.RoomCountKeyboard()

        if _type == "Участок земли":
            await Land.started.set()
            text = Messages()["land_started"]
            markup = keyboards.BackKeyboard()

        if _type == "Нежилая недвижимость":
            await Free_area.started.set()
            text = Messages()["free_area_started"]
            markup = keyboards.FreeAreaKeyboard()

        await bot.send_message(user, text, reply_markup=markup)

    elif my_state in "User:photo":

        text = Messages()["ammount"]
        await User.ammount_set.set()

        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    
    elif my_state in "Edit:photoNew":

        async with state.proxy() as data:

            _type = data['type']
            
            _property = data['property']
            _title = data['{} title'.format(_type)]
            _region = data['{} region'.format(_type)]
            _reference = data['{} reference'.format(_type)]
            _location = data['{} location'.format(_type)]
            try:
                _room_count = data['{} room_count'.format(_type)]
            except Exception as e:
                _room_count = 0

            try:
                _square = data['{} square'.format(_type)]
            except Exception as e:
                _square = 0

            
            
            try:
                _area = data['{} area'.format(_type)]
            except Exception as e:
                _area = 0
            
            try:
                _state = data['{} state'.format(_type)]
            except Exception as e:
                _state = ""

            _ammount = data['ammount']
            _add_info = data['add_info']
            _contact = data['phone']



            user_data = []
            user_data.append(_type)
            user_data.append(_property)
            user_data.append(_title)
            user_data.append(_region)
            user_data.append(_reference)
            user_data.append(_location)
            user_data.append(_room_count)
            user_data.append(_square)
            user_data.append(_area)
            user_data.append(_state)
            user_data.append(_ammount)
            user_data.append(_add_info)
            user_data.append(_contact)

            try:
                _online_status = data["online"]
                user_data.append(data['master'])

                text = OnlineGenerateEndText(user_data)
            except Exception as e:
                text = GenerateEndText(user_data, False)


        await User.edit.set()

        if _location != "0 0":
            X = _location.split(" ")[0]
            Y = _location.split(" ")[1]
            await bot.send_chat_action(user, action="find_location")

            await bot.send_location(user, latitude=X, longitude=Y)

        photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
        media = []
        for photo in photoes:
            media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
        

        markup = keyboards.EditApplyKeyboard()
        if len(media)!=1:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_media_group(user, media)
        else:
            await bot.send_chat_action(user, action="upload_photo")
            await bot.send_photo(user, InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photoes[0]))
        await bot.send_message(user, text, reply_markup=markup)

        
    
    elif my_state in "User:add_info":

        text = Messages()["contacts"]
        await User.contact.set()

        markup = keyboards.ContactKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

        




@dp.message_handler(state=User.started)
async def language_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text


    if recieved_text == "Русский язык" or recieved_text== "O`zbek tili":
        if recieved_text == "Русский язык":
            client.userSetLanguage(user, "RU")
        else:
            client.userSetLanguage(user, "UZ")

        await User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        await state.set_data({})


        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=User.language_set)
async def menu_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text == "Продажа":
        async with state.proxy() as data:
            data['type'] = "sale"

        await Sale.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif recieved_text == "Аренда":
        async with state.proxy() as data:
            data['type'] = "rent"

        await Rent.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif recieved_text == "Онлайн риелтор":
        async with state.proxy() as data:
            data['online'] = "True"

        await Online.started.set()

        text = "Выберите действие"
        markup = keyboards.OnlineSaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Online.started)
async def online_started_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in ["Продажа"]:

        async with state.proxy() as data:
            data['type'] = "sale"

        await Online.mode.set()

        text = "Выберите действие"
        markup = keyboards.OnlineKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
        
    elif recieved_text in ["Аренда"]:

        async with state.proxy() as data:
            data['type'] = "rent"

        await Online.mode.set()

        text = "Выберите действие"
        markup = keyboards.OnlineKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif recieved_text in ["Поиск"]:
        
        async with state.proxy() as data:
            data['type'] = "search"

        await Online.mode.set()

        text = "Выберите действие"
        markup = keyboards.OnlineKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Online.mode)
async def online_mode_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    online_list = []
    for a in client.api_models.OnlineRieltor.obects.all():
        online_list.append(a.name)

    if recieved_text in online_list:
        await Online.order.set()

        async with state.proxy() as data:
            data['master'] = recieved_text

        await bot.send_chat_action(user, action="upload_photo")

        photo = await client.getRieltorPhoto(recieved_text)
        photo = str(os.getcwd()).replace("bot","")+"bothelper/media/{}".format(str(photo).replace("/","/"))
        
        description = await client.getRieltorDescription(recieved_text)

        await bot.send_photo(user, InputFile(photo), caption=description)
        

        text = "Выберите действие"
        markup = keyboards.OnlineKeyboardApply()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Online.order)
async def online_order_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in ["Сделать заказ"]:
        async with state.proxy() as data:
            sub_type = data['type']
        if sub_type == "rent":
            await Rent.announcement.set()
        elif sub_type == "sale":
            await Sale.announcement.set()
        elif sub_type == "search":
            await OnlineSearch.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=OnlineSearch.announcement)
async def Search_type_choosen_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in keyboards.SaleSearchAndannouncementKeyboardList:

        MessageDict = {'Участок': Messages()['area'], 'Квартира': Messages()['flat'], 'Участок земли': Messages()['land'], 'Нежилая недвижимость': Messages()['free_area']}

        await OnlineSearch.type_choosen.set()

        async with state.proxy() as data:
            data['property'] = message.text
            
        text = MessageDict[recieved_text]
        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=OnlineSearch.type_choosen)
async def Search_title_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await OnlineSearch.title_added.set()

    async with state.proxy() as data:
        data["search title"] = recieved_text

    text = Messages()["title_added"]
    markup = keyboards.RegionKeyboard()
    try:
        await bot.send_message(user, text, reply_markup=markup)
    except Exception as e:
        print("\n\n{}\n\n".format(e))

@dp.message_handler(state=OnlineSearch.title_added)
async def Search_region_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await OnlineSearch.region_added.set()

    async with state.proxy() as data:
        data["search region"] = recieved_text

    text = Messages()["region_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=OnlineSearch.region_added)
async def Search_reference_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await OnlineSearch.reference.set()

    async with state.proxy() as data:
        data["search reference"] = recieved_text

    text = Messages()["geo1"]
    await bot.send_message(user, text)

    text = Messages()["geo2"]
    await bot.send_message(user, text)

    text = Messages()["geo3"]
    markup = keyboards.LocationKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=OnlineSearch.reference, content_types=types.ContentType.LOCATION)
async def Search_location_added_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await OnlineSearch.location_True_or_False.set()

    async with state.proxy() as data:
        data["search location"] = "{} {}".format(message.location.latitude, message.location.longitude)

        _type = data['property']

    if _type == "Участок":
        await Area.started.set()
        text = Messages()["area_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Квартира":
        await Flat.started.set()
        text = Messages()["flat_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Участок земли":
        await Land.started.set()
        text = Messages()["land_started"]
        markup = keyboards.BackKeyboard()

    if _type == "Нежилая недвижимость":
        await Free_area.started.set()
        text = Messages()["free_area_started"]
        markup = keyboards.FreeAreaKeyboard()


    await bot.send_message(user, text, reply_markup=markup)


    
@dp.message_handler(state=Rent.started)
async def rent_handler(message: types.Message):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in ["Подать объявление"]:
        await Rent.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    elif recieved_text in ["Поиск"]:
        await Rent.search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.announcement)
async def rent_type_choosen_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in keyboards.SaleSearchAndannouncementKeyboardList:

        MessageDict = {'Участок': Messages()['area'], 'Квартира': Messages()['flat'], 'Участок земли': Messages()['land'], 'Нежилая недвижимость': Messages()['free_area']}

        await Rent.type_choosen.set()

        async with state.proxy() as data:
            data['property'] = message.text
            
        text = MessageDict[recieved_text]
        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.type_choosen)
async def rent_title_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Rent.title_added.set()

    async with state.proxy() as data:
        data["rent title"] = recieved_text

    text = Messages()["title_added"]
    markup = keyboards.RegionKeyboard()
    try:
        await bot.send_message(user, text, reply_markup=markup)
    except Exception as e:
        print("\n\n{}\n\n".format(e))

@dp.message_handler(state=Rent.title_added)
async def rent_region_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Rent.region_added.set()

    async with state.proxy() as data:
        data["rent region"] = recieved_text

    text = Messages()["region_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.region_added)
async def rent_reference_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Rent.reference.set()

    async with state.proxy() as data:
        data["rent reference"] = recieved_text

    text = Messages()["geo1"]
    await bot.send_message(user, text)

    text = Messages()["geo2"]
    await bot.send_message(user, text)

    text = Messages()["geo3"]
    markup = keyboards.LocationKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.reference, content_types=types.ContentType.LOCATION)
async def rent_location_added_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Rent.location_True_or_False.set()

    async with state.proxy() as data:
        data["rent location"] = "{} {}".format(message.location.latitude, message.location.longitude)

        _type = data['property']

    if _type == "Участок":
        await Area.started.set()
        text = Messages()["area_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Квартира":
        await Flat.started.set()
        text = Messages()["flat_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Участок земли":
        await Land.started.set()
        text = Messages()["land_started"]
        markup = keyboards.BackKeyboard()

    if _type == "Нежилая недвижимость":
        await Free_area.started.set()
        text = Messages()["free_area_started"]
        markup = keyboards.FreeAreaKeyboard()


    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.started)
async def sale_handler(message: types.Message):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in ["Подать объявление"]:
        await Sale.announcement.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif recieved_text in ["Поиск"]:
        await Sale.search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.search)
async def sale_search_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    await Search.started.set()

    async with state.proxy() as data:
        data['property'] = message.text


    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(message.text)
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.search)
async def rent_search_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    await Search.started.set()

    async with state.proxy() as data:
        data['property'] = message.text


    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(message.text)
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Search.started)
async def data_search_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text
    markup = keyboards.BackKeyboard()
    
    text = "Отправьте текст"

    if recieved_text == "Цена":
        text = Messages()["price_list"]
        markup = keyboards.PriceSetKeyboard()

        await Search.price.set()
        await bot.send_message(user, text, reply_markup=markup)


    elif recieved_text == "Район":
        await Search.region.set()
        markup = keyboards.RegionKeyboard()
        await bot.send_message(user, text, reply_markup=markup)


    elif recieved_text == "Комнаты":
        await Search.room_count.set()
        markup = keyboards.RoomCountKeyboard()
        await bot.send_message(user, text, reply_markup=markup)


    elif recieved_text == "Сотки":
        await Search.area.set()
        await bot.send_message(user, text, reply_markup=markup)

    elif recieved_text == "Поиск":
        search_data = {}

        async with state.proxy() as data:
            
            try:
                search_data["type"] = data["type"]
            except Exception as e:
                search_data["type"] = ""
            try:
                search_data["property"] = data["property"]
            except Exception as e:
                search_data["property"] = ""
            try:
                search_data["price"] = data["search price"]
            except Exception as e:
                search_data["price"] = ""
            try:
                search_data["region"] = data["search region"]
            except Exception as e:
                search_data["region"] = ""
            try:
                search_data["room_count"] = data["search room_count"]
            except Exception as e:
                search_data["room_count"] = ""
            try:
                search_data["area"] = data["search area"]
            except Exception as e:
                search_data["area"] = ""
            

        orders = await SearchAnnouncement(search_data)
        if len(orders)!=0:
            for order in orders:

                _ann_number = order.id
                _type = order._type
                _property = order._property
                _title = order.title
                _region = order.region
                _reference = order.reference
                _location = '{} {}'.format(order.location_X, order.location_Y)
                _room_count = order.room_count

                _square = order.square
                _area = order.area
                
                _state = order.state

                _ammount = order.ammount
                _add_info = order.add_info
                _contact = order.contact



                user_data = []
                user_data.append(_type)
                user_data.append(_property)
                user_data.append(_title)
                user_data.append(_region)
                user_data.append(_reference)
                user_data.append(_location)
                user_data.append(_room_count)
                user_data.append(_square)
                user_data.append(_area)
                user_data.append(_state)
                user_data.append(_ammount)
                user_data.append(_add_info)
                user_data.append(_contact)
                user_data.append(_ann_number)


                text = GenerateEndText(user_data, True)
                if _location != "0 0":
                    X = _location.split(" ")[1]
                    Y = _location.split(" ")[0]
                    await bot.send_chat_action(user, action="find_location")

                    await bot.send_location(user, latitude=X, longitude=Y)

                ann_photoes = order.photo.all()
                if len(ann_photoes)!=1:

                    media = []

                    for photo in ann_photoes:
                        photoToUpload = str(os.getcwd()).replace("bot","")+"bothelper/media/{}".format(str(photo).replace("/","/"))
                        media.append(InputMediaPhoto((InputFile(photoToUpload))))

                    await bot.send_media_group(user, media)
                else:
                    photoToUpload = str(os.getcwd()).replace("bot","")+"bothelper/media/{}".format(str(ann_photoes[0]).replace("/","/"))

                    await bot.send_photo(user, InputFile(photoToUpload))



                

                # photoes = os.listdir(os.getcwd()+"/Users/" + str(user)+"/")
                # media = []
                # for photo in photoes:
                #     media.append(InputMediaPhoto((InputFile(os.getcwd()+"/Users/" + str(user)+"/"+photo))))
                
                # await bot.send_media_group(user, media)

                
                await bot.send_message(user, text, reply_markup=None)
        else:
            text = "Объявлений не найдено"
            await bot.send_message(user, text, reply_markup=None)


    
        

@dp.message_handler(state=Search.price)
async def search_price_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text
    if recieved_text=="1":
        price = "25000"
    elif recieved_text=="2":
        price = "25000 50000"
    elif recieved_text=="3":
        price = "50000 75000"
    elif recieved_text=="4":
        price = "100000"


    async with state.proxy() as data:
        data['search price'] = price
        prop = data['property']


    await Search.started.set()

    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(prop)
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Search.region)
async def search_region_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text
    async with state.proxy() as data:
        data['search region'] = recieved_text
        prop = data['property']
    await Search.started.set()


    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(prop)
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Search.room_count)
async def search_room_count_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text
    async with state.proxy() as data:
        data['search room_count'] = recieved_text
        prop = data['property']

    await Search.started.set()


    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(prop)
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Search.area)
async def search_area_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text
    async with state.proxy() as data:
        data['search area'] = recieved_text
        prop = data['property']

    await Search.started.set()


    text = "Установите фильтр"
    markup = keyboards.SearchKeyboard(prop)
    await bot.send_message(user, text, reply_markup=markup)
   

@dp.message_handler(state=Sale.announcement)
async def sale_type_choosen_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in keyboards.SaleSearchAndannouncementKeyboardList:

        MessageDict = {'Участок': Messages()['area'], 'Квартира': Messages()['flat'], 'Участок земли': Messages()['land'], 'Нежилая недвижимость': Messages()['free_area']}

        await Sale.type_choosen.set()

        async with state.proxy() as data:
            data['property'] = message.text
            
        text = MessageDict[recieved_text]
        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.type_choosen)
async def sale_title_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Sale.title_added.set()

    async with state.proxy() as data:
        data["sale title"] = recieved_text

    text = Messages()["title_added"]
    markup = keyboards.RegionKeyboard()
    try:
        await bot.send_message(user, text, reply_markup=markup)
    except Exception as e:
        print("\n\n{}\n\n".format(e))

@dp.message_handler(state=Sale.title_added)
async def sale_region_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Sale.region_added.set()

    async with state.proxy() as data:
        data["sale region"] = recieved_text

    text = Messages()["region_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.region_added)
async def sale_reference_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Sale.reference.set()

    async with state.proxy() as data:
        data["sale reference"] = recieved_text

    text = Messages()["geo1"]
    await bot.send_message(user, text)

    text = Messages()["geo2"]
    await bot.send_message(user, text)

    text = Messages()["geo3"]
    markup = keyboards.LocationKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.reference, content_types=types.ContentType.LOCATION)
async def sale_location_added_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Sale.location_True_or_False.set()

    async with state.proxy() as data:
        data["sale location"] = "{} {}".format(message.location.latitude, message.location.longitude)

        _type = data['property']

    if _type == "Участок":
        await Area.started.set()
        text = Messages()["area_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Квартира":
        await Flat.started.set()
        text = Messages()["flat_started"]
        markup = keyboards.RoomCountKeyboard()

    if _type == "Участок земли":
        await Land.started.set()
        text = Messages()["land_started"]
        markup = keyboards.BackKeyboard()

    if _type == "Нежилая недвижимость":
        await Free_area.started.set()
        text = Messages()["free_area_started"]
        markup = keyboards.FreeAreaKeyboard()


    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Area.started)
async def sale_area_room_count_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Area.square.set()

    async with state.proxy() as data:
        data["sale room_count"] = recieved_text

    text = Messages()["area_rooms_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Area.square)
async def sale_area_square_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Area.area.set()

    async with state.proxy() as data:
        data["sale square"] = recieved_text

    text = Messages()["area_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Area.area)
async def sale_area_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await User.photo.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["photo1"]
    await bot.send_message(user, text, reply_markup=None)

    text = Messages()["photo2"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=User.photo, content_types=types.ContentType.PHOTO)
async def sale_area_photo_added_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id

    count = len(os.listdir(os.getcwd()+"/Users/" + str(user)+"/"))

    if count+1<10:
        text = Messages()["photo3"].format(count+1)

        photo = await bot.get_file(message.photo[-1].file_id)
        await photo.download(os.getcwd()+"/Users/" + str(user)+"/{}.jpg".format(message.photo[-1].file_id))

        markup = keyboards.BackNextKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    else:
        text = Messages()["ammount"]
        await User.ammount_set.set()
        

        markup = keyboards.BackKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    


@dp.message_handler(state=Flat.started)
async def sale_flat_room_count_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Flat.square.set()

    async with state.proxy() as data:
        data["sale room_count"] = recieved_text

    text = Messages()["flat_rooms_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Flat.square)
async def sale_flat_square_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await User.photo.set()

    async with state.proxy() as data:
        data["sale square"] = recieved_text

    text = Messages()["photo1"]
    await bot.send_message(user, text, reply_markup=None)

    text = Messages()["photo2"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(state=Land.started)
async def sale_land_square_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Land.square.set()

    async with state.proxy() as data:
        data["sale square"] = recieved_text

    text = Messages()["land_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Land.square)
async def sale_land_area_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await User.photo.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["photo1"]
    await bot.send_message(user, text, reply_markup=None)

    text = Messages()["photo2"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.started)
async def sale_free_area_room_count_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.square.set()

    async with state.proxy() as data:
        data["sale state"] = recieved_text

    text = Messages()["free_area_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)



@dp.message_handler(state=Free_area.state)
async def sale_free_area_square_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.square.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["free_area_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.square)
async def sale_free_area_area_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await User.photo.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["photo1"]
    await bot.send_message(user, text, reply_markup=None)

    text = Messages()["photo2"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)






@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])


@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])

    if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=argument))

    await state.set_state(TestStates.all()[int(argument)])
    await message.reply(MESSAGES['state_change'], reply=False)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    if not os.path.exists(os.getcwd()+"/Users/"):
        os.mkdir(os.getcwd()+"/Users/", 0o777)
        
    executor.start_polling(dp, on_shutdown=shutdown)