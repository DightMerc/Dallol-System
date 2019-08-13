from django.urls import path
from .user_views import UserCreateView, UserUpdateView, ListUsersView
from .product_view import ListCategoryView, ListProductView
from .order_view import ListOrdersView, OrderCreateView

urlpatterns = [

    path('users/', ListUsersView.as_view(), name="users-all"),
    path('users/create/', UserCreateView.as_view(), name="user-create"),
    path('users/<int:telegram_id>/update/', UserUpdateView.as_view(),name="user-update"),

    path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('orders/create/', OrderCreateView.as_view(), name="order-create"),

    path('products/', ListProductView.as_view(), name="products-all"),
    path('cats/', ListCategoryView.as_view(), name="cats-all"),
    
]