from rest_framework import serializers
from .models import TelegramUser
from .models import Order
from .models import Product
from .models import Category



class UserSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    phone = serializers.IntegerField(required=False)


    def create(self, validated_data):
        return TelegramUser.objects.create(**validated_data)

class UserPhoneSerializer(serializers.Serializer):
    phone = serializers.IntegerField()

    def create(self, validated_data):
        return TelegramUser.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'published_date', 'products')

    def create(self, validated_data):
        products = validated_data.pop('products')
        instance = Order.objects.create(**validated_data)
        for product in products:
            instance.products.add(product)

        return instance
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'available', 'category', 'description', 'photo', 'price')