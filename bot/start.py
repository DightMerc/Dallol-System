import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from utils import TestStates
from messages import Messages

import client

import keyboards
from typing import Optional
import os



logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                     level=logging.DEBUG)



bot = Bot(token="796303915:AAF4MJs2lqEYxUWtK-7VSjYVWGjeLhNEXnU")
storage = RedisStorage2(db=5)
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())




# States
class User(StatesGroup):
    started = State() 
    language_set = State() 
    test_state = State()



class Sale(StatesGroup):
    started = State()
    announcement_or_search = State()
    type_choosen = State()
    title_added = State()
    region_added = State()
    reference = State()
    location_True_or_False = State()

class Area(StatesGroup):
    started = State()
    square = State()
    area = State()
    photo = State()



class Flat(StatesGroup):
    started = State()
    square = State()
    area = State()
    photo = State()

class Land(StatesGroup):
    started = State()
    square = State()
    area = State()
    photo = State()

class Free_area(StatesGroup):
    started = State()
    square = State()
    state = State()
    photo = State()




class Rent(StatesGroup):
    started = State()
    announcement_or_search = State()
    type_choosen = State()
    title_added = State()
    region_added = State()
    reference = State()
    location_True_or_False = State()




@dp.message_handler(commands=['start'], state="*")
async def process_start_command(message: types.Message):
    user = message.from_user.id

    if not os.path.exists(os.getcwd()+"\\Users\\" + str(user)):
        os.mkdir(os.getcwd()+"\\Users\\" + str(user), 0o777)

    if not client.userExsists(user):
        client.userCreate(message.from_user)

    
    await User.started.set()
    
    await bot.send_message(user, Messages()['start'].format(message.from_user.first_name))
    await bot.send_message(user, Messages()['language'], reply_markup=keyboards.LanguageKeyboard())

@dp.message_handler(commands=['state'], state="*")
async def get_MyState(message: types.Message):
    user = message.from_user.id

    state = await dp.current_state(user=message.from_user.id).get_state()

    await bot.send_message(user, state)

@dp.message_handler(text="Назад", state="*")
async def back_handler(message: types.Message):
    user = message.from_user.id
    state = await dp.current_state(user=message.from_user.id).get_state()

    if state in ["Sale:started", "Rent:started"]:

        await User.language_set.set()

        text = "Выберите действие"
        markup = keyboards.MenuKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

    elif state == "Sale:announcement_or_search":

        await Sale.started.set()

        text = "Выберите действие"
        markup = keyboards.SaleAndRentKeyboard()
        await bot.send_message(user, text, reply_markup=markup)
    
    elif state == "Sale:type_choosen":

        await Sale.announcement_or_search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(text="Дальше", state="*")
async def get_MyState(message: types.Message, state: FSMContext):
    user = message.from_user.id
    my_state = await dp.current_state(user=message.from_user.id).get_state()

    if my_state in "Rent:reference":
        user = message.from_user.id
        recieved_text = message.text

        await Rent.location_True_or_False.set()

        async with state.proxy() as data:
            data["rent location"] = "None"

            _type = data['type_choosen']

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
            data["sale location"] = "None"

            _type = data['type_choosen']

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




@dp.message_handler(state=User.started)
async def language_handler(message: types.Message):
    user = message.from_user.id
    recieved_text = message.text


    if recieved_text == "Русский язык" or recieved_text== "O`zbek tili":
        if recieved_text == "Русский язык":
            client.userSetLanguage(user, "RU")
        else:
            client.userSetLanguage(user, "UZ")

        await User.language_set.set()

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

@dp.message_handler(state=Rent.started)
async def rent_handler(message: types.Message):
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in ["Подать объявление", "Поиск"]:
        await Rent.announcement_or_search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Rent.announcement_or_search)
async def rent_type_choosen_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in keyboards.SaleSearchAndannouncementKeyboardList:

        MessageDict = {'Участок': Messages()['area'], 'Квартира': Messages()['flat'], 'Участок земли': Messages()['land'], 'Нежилая недвижимость': Messages()['free_area']}

        await Rent.type_choosen.set()

        async with state.proxy() as data:
            data['type_choosen'] = message.text
            
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

        _type = data['type_choosen']

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

    if recieved_text in ["Подать объявление", "Поиск"]:
        await Sale.announcement_or_search.set()

        text = "Выберите действие"
        markup = keyboards.SaleSearchAndannouncementKeyboard()
        await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Sale.announcement_or_search)
async def sale_type_choosen_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    if recieved_text in keyboards.SaleSearchAndannouncementKeyboardList:

        MessageDict = {'Участок': Messages()['area'], 'Квартира': Messages()['flat'], 'Участок земли': Messages()['land'], 'Нежилая недвижимость': Messages()['free_area']}

        await Sale.type_choosen.set()

        async with state.proxy() as data:
            data['type_choosen'] = message.text
            
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

        _type = data['type_choosen']

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

    await Area.photo.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["photo1"]
    await bot.send_message(user, text, reply_markup=None)

    text = Messages()["photo2"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Area.photo, content_types=types.ContentType.PHOTO)
async def sale_area_photo_added_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id
    recieved_text = message.text

    photo = await bot.get_file(message.photo[-1].file_id)
    await photo.download(os.getcwd()+"\\Users\\" + str(user)+"\\{}.jpg".format(message.photo[-1].file_id))

    text = "Принято"
    markup = None
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Flat.photo, content_types=types.ContentType.PHOTO)
async def sale_flat_photo_added_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    photo = await bot.get_file(message.photo[-1].file_id)
    await photo.download(os.getcwd()+"\\Users\\" + str(user)+"\\{}.jpg".format(message.photo[-1].file_id))

    text = "Принято"
    markup = None
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Land.photo, content_types=types.ContentType.PHOTO)
async def sale_flat_photo_added_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    photo = await bot.get_file(message.photo[-1].file_id)
    await photo.download(os.getcwd()+"\\Users\\" + str(user)+"\\{}.jpg".format(message.photo[-1].file_id))

    text = "Принято"
    markup = None
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.photo, content_types=types.ContentType.PHOTO)
async def sale_flat_photo_added_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    photo = await bot.get_file(message.photo[-1].file_id)
    await photo.download(os.getcwd()+"\\Users\\" + str(user)+"\\{}.jpg".format(message.photo[-1].file_id))

    text = "Принято"
    markup = None
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Flat.photo, content_types=types.ContentType.PHOTO)
async def sale_flat_photo_added_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    photo = await bot.get_file(message.photo[-1].file_id)
    await photo.download(os.getcwd()+"\\Users\\" + str(user)+"\\{}.jpg".format(message.photo[-1].file_id))

    text = "Принято"
    markup = None
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

    await Flat.photo.set()

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

    await Land.photo.set()

    async with state.proxy() as data:
        data["sale area"] = recieved_text

    text = Messages()["land_square_added"]
    markup = keyboards.FreeAreaKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.started)
async def sale_free_area_room_count_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.square.set()

    async with state.proxy() as data:
        data["sale square"] = recieved_text

    text = Messages()["free_area_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.started)
async def sale_free_area_state_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.state.set()

    async with state.proxy() as data:
        data["sale state"] = recieved_text

    text = Messages()["free_area_state_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.state)
async def sale_free_area_square_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.square.set()

    async with state.proxy() as data:
        data["sale square"] = recieved_text

    text = Messages()["free_area_square_added"]
    markup = keyboards.BackKeyboard()
    await bot.send_message(user, text, reply_markup=markup)

@dp.message_handler(state=Free_area.square)
async def sale_free_area_area_handler(message: types.Message, state: FSMContext):
    
    user = message.from_user.id
    recieved_text = message.text

    await Free_area.photo.set()

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
    if not os.path.exists(os.getcwd()+"\\Users\\"):
        os.mkdir(os.getcwd()+"\\Users\\", 0o777)
        
    executor.start_polling(dp, on_shutdown=shutdown)