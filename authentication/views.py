from re import A
from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionDenied
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework.compat import requests
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.prefetch_related('transactions')
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer
    
    #recupera o objeto que está vindo da requisição
    def get_object(self):
        obj = super().get_object()

        if obj.id != self.request.user.id:
            raise PermissionDenied('Você não pode alterar dados de outro usuário')

        return obj


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def get_object(self):
        obj = super().get_object()

        if obj.id != self.request.user.id:
            raise PermissionDenied('Você não tem permissão para alterar outro usuário')

        return obj

