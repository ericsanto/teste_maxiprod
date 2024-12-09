import email
from django.contrib.auth import get_user_model
from rest_framework import response
from rest_framework.response import responses
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import datetime
from authentication.models import UserCustom


class UrlTesteCase(APITestCase):
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.url_list_users = '/api/v1/users/all/'
        self.url_post_user = '/api/v1/authentication/register/'
        self.url_obtain_token = '/api/v1/authentication/token/'
        self.user = {
                "username":"eric",
                "password":"12345teste",
                "date_of_birth": datetime.date(2002, 4, 12),
                "email":"eric@gmail.com"
                }

        self.user_custom = UserCustom.objects.create(
            username="eric",
            email="eric@gmail.com",
            date_of_birth=datetime.date(2002, 4, 12),
        )

        self.user_update_data = {
            "username": "eric_updated",
            "email": "eric_updated@gmail.com",
            "date_of_birth": datetime.date(2002, 4, 12),
        }

        self.url_update_user = f'/api/v1/user/update/{self.user_custom.id}/'

        self.token = self.get_token()

    def get_token(self):
        response = self.client.post(self.url_post_user, self.user)
        
        if response.status_code == 200:
            return response.data["access"]
        return None

    def test_get_request_url_setup(self):
        response = self.client.get(self.url_list_users)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_request_url_setup(self):
        self.client.post(
                self.url_post_user,
                self.user,
                )

        response = self.client.get(self.url_list_users)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserCustom.objects.get().username, self.user["username"])
    
