from django.shortcuts import render, get_object_or_404

from .models import TelegramUser

from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.db import IntegrityError

class ListUsersView(APIView):
    def get(self, request, version):
        users = TelegramUser.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})
    
class UserCreateView(APIView):
    def post(self, request, version):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user_created = serializer.save()
                return Response({"success": "{} User '{}' created successfully".format(user_created.id, user_created.telegram_id)}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)

class UserUpdateView(APIView):
    def post(self, request, version, telegram_id):

        phone = request.data["phone"]

        try:
            update = get_object_or_404(TelegramUser, telegram_id=telegram_id)
            update.phone = phone
            update.save()

            return Response({"success": "{} User number'{}' successfully set".format(update.id, phone)}, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({"error": str(e) + str(phone)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


