from django.contrib import admin
from .models import TemporaryOrder, Order, TelegramUser, Photo, OnlineRieltor, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, CommonRieltorUser

# Register your models here.
# admin.site.register(Order)
admin.site.register(TemporaryOrder)
# admin.site.register(TelegramUser)
admin.site.register(Photo)
admin.site.register(OnlineRieltor)
admin.site.register(OnlineRieltorTemporaryOrder)
# admin.site.register(OnlineRieltorOrder)
admin.site.register(CommonRieltorUser)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'active','type', 'property', 'ammount', 'region', 'contact')
    ordering = ('active',)
    search_fields = ('type', 'property', 'ammount', 'region')

@admin.register(OnlineRieltorOrder)
class OnlineOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'rieltor','type', 'property', 'ammount', 'region')
    ordering = ('active',)
    search_fields = ('type', 'property', 'ammount', 'region')

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'phone', 'language','full_name', 'created_date')
    ordering = ('telegram_id',)
    search_fields = ('telegram_id', 'phone', 'language')