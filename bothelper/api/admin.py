from django.contrib import admin
from .models import TemporaryOrder, Order, TelegramUser, Photo, OnlineRieltor

# Register your models here.
admin.site.register(Order)
admin.site.register(TemporaryOrder)
admin.site.register(TelegramUser)
admin.site.register(Photo)
admin.site.register(OnlineRieltor)
