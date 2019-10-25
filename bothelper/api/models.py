from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
 
class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField("Telegram ID", default=0, unique=True, null=False)
    full_name = models.CharField("Name", max_length=255, default="", null=False)
    username = models.CharField("Username", max_length=255, default="", null=True)
    phone = models.PositiveIntegerField("Phone Number", null=True, blank=True)

    language = models.CharField("Язык", max_length=5, default="RU")

    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.telegram_id)

class Photo(models.Model):
    title = models.CharField("Название", max_length=255, default="", null=False)
    photo = models.ImageField("Фото", upload_to='media/')

    def __str__(self):
        return self.title
    

class TemporaryOrder(models.Model):

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)

    type = models.CharField("Операция", max_length=10)
    property = models.CharField("Тип недвижимости", max_length=30)
    title = models.TextField("Описание")
    region = models.CharField("Район", max_length=30)
    reference = models.CharField("Ориентир", max_length=30)
    location_X = models.FloatField("Локация: широта")
    location_Y = models.FloatField("Локация: долгота")
    room_count = models.PositiveIntegerField("Количество комнат")
    square = models.FloatField("Общая площадь")
    area = models.FloatField("Количество соток")
    main_floor = models.PositiveIntegerField("Количество этажей в доме")
    floor = models.PositiveIntegerField("Этаж квартиры")
    state = models.CharField("Состояние", max_length=30)
    ammount = models.CharField("Цена", max_length=255)
    add_info = models.TextField("Инфо")
    contact = models.PositiveIntegerField("Номер телефона")

    photo = models.ManyToManyField(Photo)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(str(self.id), str(self.type), str(self.property))




class OnlineRieltor(models.Model):
    name = models.CharField("ФИО", max_length=255)

    photo = models.ImageField("Фото", upload_to='media/')
    active = models.BooleanField("Активно", default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField("Описание РУС")

    description_UZ = models.TextField("Описание УЗБ")


    def __str__(self):
        return str(self.name)


class OnlineRieltorTemporaryOrder(models.Model):

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)

    rieltor = models.ForeignKey(OnlineRieltor, on_delete=models.CASCADE)
    type = models.CharField("Операция", max_length=10)
    property = models.CharField("Тип недвижимости", max_length=30)
    title = models.TextField("Описание")
    region = models.CharField("Район", max_length=30)
    reference = models.CharField("Ориентир", max_length=30)
    location_X = models.FloatField("Локация: широта")
    location_Y = models.FloatField("Локация: долгота")
    room_count = models.CharField("Количество комнат", max_length=255)
    square = models.CharField("Общая площадь", max_length=255)
    area = models.CharField("Количество соток", max_length=255)
    main_floor = models.CharField("Количество этажей в доме", max_length=255)
    floor = models.CharField("Этаж квартиры", max_length=255)
    state = models.CharField("Состояние", max_length=30)
    main_state = models.CharField("Состояние ремонта", max_length=30)

    ammount = models.CharField("Цена", max_length=255)
    add_info = models.TextField("Инфо")
    contact = models.PositiveIntegerField("Номер телефона")

    photo = models.ManyToManyField(Photo)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(str(self.id), str(self.type), str(self.property))

class OnlineRieltorOrder(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)

    pro_order = models.ForeignKey(OnlineRieltorTemporaryOrder, on_delete=models.CASCADE)

    active = models.BooleanField("Актуально", default=True)

    rieltor = models.ForeignKey(OnlineRieltor, on_delete=models.CASCADE)

    type = models.CharField("Операция", max_length=10)
    property = models.CharField("Тип недвижимости", max_length=30)
    title = models.TextField("Описание")
    region = models.CharField("Район", max_length=30)
    reference = models.CharField("Ориентир", max_length=30)
    location_X = models.FloatField("Локация: широта")
    location_Y = models.FloatField("Локация: долгота")
    room_count = models.CharField("Количество комнат", max_length=255)
    square = models.CharField("Общая площадь", max_length=255)
    area = models.CharField("Количество соток", max_length=255)
    main_floor = models.CharField("Количество этажей в доме", max_length=255)
    floor = models.CharField("Этаж квартиры", max_length=255)
    state = models.CharField("Состояние", max_length=30)
    main_state = models.CharField("Состояние ремонта", max_length=30)

    ammount = models.CharField("Цена", max_length=255)
    add_info = models.TextField("Инфо")
    contact = models.PositiveIntegerField("Номер телефона")

    photo = models.ManyToManyField(Photo)

    created_date = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return "{} {} {}".format(str(self.id), str(self.type), str(self.property))

class Order(models.Model):

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)

    pro_order = models.ForeignKey(TemporaryOrder, on_delete=models.CASCADE)

    active = models.BooleanField("Актуально", default=True)

    type = models.CharField("Операция", max_length=10)
    property = models.CharField("Тип недвижимости", max_length=30)
    title = models.TextField("Описание")
    region = models.CharField("Район", max_length=30)
    reference = models.CharField("Ориентир", max_length=30)
    location_X = models.FloatField("Локация: широта")
    location_Y = models.FloatField("Локация: долгота")
    room_count = models.PositiveIntegerField("Количество комнат")
    square = models.FloatField("Общая площадь")
    area = models.FloatField("Количество соток")
    main_floor = models.PositiveIntegerField("Количество этажей в доме")
    floor = models.PositiveIntegerField("Этаж квартиры")
    state = models.CharField("Состояние", max_length=30)
    ammount = models.PositiveIntegerField("Цена")
    add_info = models.TextField("Инфо")
    contact = models.PositiveIntegerField("Номер телефона")

    photo = models.ManyToManyField(Photo)

    created_date = models.DateTimeField(default=timezone.now)

    show = models.PositiveIntegerField("Количество просмотров", default=0)

    def __str__(self):
        return "{} {} {}".format(str(self.id), str(self.type), str(self.property))


class CommonRieltorUser(models.Model):

    name = models.CharField("ФИО", max_length=255)

    active = models.BooleanField("Актуально", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rieltor = models.ForeignKey(OnlineRieltor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Agency(models.Model):

    title = models.CharField("Название", max_length=255)

    active = models.BooleanField("Актуально", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rieltors = models.ManyToManyField(OnlineRieltor)

    def __str__(self):
        return str(self.title)