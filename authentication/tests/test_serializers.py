from django.test import TestCase
from rest_framework.schemas.coreapi import serializers
from authentication.serializers import RegisterSerializer, UserSerializer
import datetime

class RegisterSerializerTestCasa(TestCase):
    
    def test_invalid_data(self):
        invalid_data = {
                "username": "",
                "password": "",
                "date_of_birth":""
                }

        serializer = RegisterSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)
        self.assertIn("password", serializer.errors)
        self.assertIn("date_of_birth", serializer.errors)

    def test_valid_data(self):
        valid_data = {
                "username":"eric",
                "password":"kansaskaz2y5",
                "date_of_birth": datetime.date(2002, 4, 12)
                }

        serializer = RegisterSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["username"], "eric")
        self.assertEqual(serializer.validated_data["password"], "kansaskaz2y5")
        self.assertEqual(serializer.validated_data["date_of_birth"], datetime.date(2002, 4, 12))

