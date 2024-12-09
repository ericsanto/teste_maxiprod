from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Person
from .serializers import PersonModelSerializer
from maxiprod.permission import IsAdminOrReadyOnly

class PersonListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminOrReadyOnly]
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


class PersonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadyOnly]
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

