from time import timezone
from django.utils.formats import date_format
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.schemas.coreapi import models
from django.utils.timezone import now
from .models import UserCustom
from datetime import date, datetime

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    age = serializers.CharField(max_length=3, required=False)
    date_of_birth = serializers.DateField()
    
    class Meta:
        model = UserCustom
        fields = ('first_name','last_name','username', 'password', 'email', 'date_of_birth', 'age')
    
    
    def calculate_age(self, key):

        date_b = key['date_of_birth']

        date_now = datetime.today().date()

        quantity_difference_dates = date_now - date_b
        
        age_int = quantity_difference_dates.days
        
        print(age_int)

        totaly = age_int // 365
        age_str = str(totaly)

        return age_str
        


    def create(self, validated_data):

        age = self.calculate_age(validated_data)

        user = UserCustom.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            age=age,
            date_of_birth=validated_data['date_of_birth']
        )

        return user

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCustom 
        fields = ('id','username', 'first_name', 'last_name', 'email', 'date_of_birth', 'age')
