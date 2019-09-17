from django.contrib import admin
from .models import TemporaryOrder, Order, TelegramUser, Photo, OnlineRieltor, OnlineRieltorTemporaryOrder, OnlineRieltorOrder

# Register your models here.
admin.site.register(Order)
admin.site.register(TemporaryOrder)
admin.site.register(TelegramUser)
admin.site.register(Photo)
admin.site.register(OnlineRieltor)
admin.site.register(OnlineRieltorTemporaryOrder)
admin.site.register(OnlineRieltorOrder)

