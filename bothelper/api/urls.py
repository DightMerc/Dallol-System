from django.urls import path
from .views import StatView, OnlineStatView, OperationMoreView, OperationShowView, OperationView, OperationMoreViewCommon, OperationViewCommon, OperationShowViewCommon, InactiveCommonView, OnlineAccountView, OnlineMain

urlpatterns = [
    path("stat/", StatView, name="stat"),
    path("online/accounts/create/", OnlineAccountView, name="onlineStat"),
    path("", OnlineMain, name="onlineMain"),

    path("statistics/", OnlineStatView, name="onlineStat"),
    path("more/<str:operation>/<str:property>/<int:pk>/", OperationMoreView, name="onlineStatMore"),
    path("operation/<str:operation>/show/<int:pk>/", OperationShowView, name="onlineStatShow"),
    path("operation/common/<str:operation>/show/<int:pk>/", OperationShowViewCommon, name="onlineStatShowCommon"),
    path("announcement/<int:pk>/", OperationView, name="onlineStatOperation"),
    path("common/<int:pk>/", OperationViewCommon, name="onlineStatOperation"),
    path("common/<str:operation>/<str:property>/<int:pk>/", OperationMoreViewCommon, name="onlineStatOperation"),
    path("inactive/order/<int:pk>/", InactiveCommonView, name="onlineStatOperation"),
    
    # path("inactive/rieltororder/<int:pk>/", InactiveCommonView, name="onlineStatOperation"),


]
