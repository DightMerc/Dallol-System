from django.urls import path
from .views import StatView, OnlineStatView

urlpatterns = [
    path("stat/", StatView, name="stat"),
    path("", OnlineStatView, name="onlineStat")
]
