from django.urls import path
from .views import StatView

urlpatterns = [
    path("stat/", StatView, name="stat")
]