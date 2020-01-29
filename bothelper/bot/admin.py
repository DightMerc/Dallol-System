from django.contrib import admin
from .models import Message, PaySystem, Setting, Region, Admin, MainRegion

# Register your models here.
admin.site.register(Message)
admin.site.register(PaySystem)
admin.site.register(Setting)
admin.site.register(Region)
admin.site.register(Admin)
admin.site.register(MainRegion)



