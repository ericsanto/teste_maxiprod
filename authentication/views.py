from re import A
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from .models import UserCustom

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = UserCustom.objects.all()
    serializer_class = UserSerializer 
