from django.urls import path
from .views import StatView, OnlineStatView, OperationMoreView, OperationShowView, OperationView, OperationMoreViewCommon, OperationViewCommon, OperationShowViewCommon, InactiveCommonView, OnlineAccountView, OnlineMain
from .views import OnlineStatViewAgencySingle, OperationShowViewCommonAgency, OperationMoreViewCommonAgency, OperationMoreViewAgency, OperationViewCommonAgency, OperationShowViewAgency, OperationViewAgency
urlpatterns = [
    path("stat/", StatView, name="stat"),
    path("online/accounts/create/", OnlineAccountView, name="onlineStat"),
    path("", OnlineMain, name="onlineMain"),

    path("statistics/", OnlineStatView, name="onlineStat"),
    path("more/<str:operation>/<str:property>/<int:pk>/", OperationMoreView, name="onlineStatMore"),
    path("operation/<str:operation>/show/<int:pk>/", OperationShowView, name="onlineStatShow"),
    path("operation/common/<str:operation>/show/<int:pk>/", OperationShowViewCommon, name="onlineStatShowCommon"),
    path("announcement/<int:pk>/", OperationView, name="onlineStatOperation"),
    path("common/<int:pk>/", OperationViewCommon, name="onlineStatOperation1"),
    path("common/<str:operation>/<str:property>/<int:pk>/", OperationMoreViewCommon, name="onlineStatOperation2"),
    path("inactive/order/<int:pk>/", InactiveCommonView, name="onlineStatOperation3"),

    path("statistics/<int:pk>", OnlineStatViewAgencySingle, name="onlineStat"),
    path("operation/common/agency/<str:operation>/show/<int:pk>/<int:telegram_user>", OperationShowViewCommonAgency, name="onlineStatShowCommonAgency"),
    path("common/agency/<str:operation>/<str:property>/<int:pk>/<int:telegram_user>", OperationMoreViewCommonAgency, name="onlineStatOperationAgency"),
    path("more/agency/<str:operation>/<str:property>/<int:pk>/<int:rieltor>", OperationMoreViewAgency, name="onlineStatMoreAgency"),
    path("common/agency/<int:pk>/", OperationViewCommonAgency, name="onlineStatOperation4"),
    path("agency/operation/<str:operation>/show/<int:pk>/<int:rieltor>", OperationShowViewAgency, name="onlineStatShowAgency"),

    path("agency/announcement/<int:pk>/", OperationViewAgency, name="onlineStatOperation"),








    

    
    # path("inactive/rieltororder/<int:pk>/", InactiveCommonView, name="onlineStatOperation"),


]
