from django.contrib import admin
from .models import TemporaryOrder, Order, TelegramUser, Photo, OnlineRieltor, OnlineRieltorTemporaryOrder, OnlineRieltorOrder, CommonRieltorUser, Agency

# Register your models here.
# admin.site.register(Order)
admin.site.register(TemporaryOrder)
# admin.site.register(TelegramUser)
admin.site.register(Photo)
admin.site.register(OnlineRieltor)
admin.site.register(OnlineRieltorTemporaryOrder)
# admin.site.register(OnlineRieltorOrder)





@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'active','type', 'property', 'user', 'region', 'contact')
    ordering = ('active',)
    search_fields = ('type', 'property', 'ammount', 'region', "user")

@admin.register(CommonRieltorUser)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','user', 'rieltor')
    ordering = ('active',)
    search_fields = ('id', 'name','user', 'rieltor')

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

@admin.register(Agency)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'user')
    ordering = ('user',)
    search_fields = ('title', 'active', 'user')
