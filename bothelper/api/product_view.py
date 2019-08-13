from django.shortcuts import render

from .models import Category, Product

from .serializers import CategorySerializer, ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.db import IntegrityError


class ListCategoryView(APIView):
    def get(self, request, version):
        cats = Category.objects.all()
        
        serializer = CategorySerializer(cats, many=True)
        return Response({"categories": serializer.data})

    
class ListProductView(APIView):
    def get(self, request, version):
        products = Product.objects.all()
        
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})