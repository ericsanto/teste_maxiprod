from django.urls import path
from .views import PersonListCreateAPIView, PersonRetrieveUpdateDestroyAPIView

urlpatterns = [
    
        path('users/', PersonListCreateAPIView.as_view(), name='users'),
        path('user/<int:pk>', PersonRetrieveUpdateDestroyAPIView.as_view(), name='update_delete_user')

        ]
