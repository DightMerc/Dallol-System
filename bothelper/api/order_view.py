from django.shortcuts import render

from .models import Order

from .serializers import OrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.db import IntegrityError



class OrderCreateView(APIView):
    def post(self, request, version):

        # Create an article from the above data
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                order_created = serializer.save()
                return Response({"success": "Order created successfully"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


class ListOrdersView(APIView):
    def get(self, request, version):
        orders = Order.objects.all()
        
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})