from django.urls import path
from .views import FinancialTransactionListAPIView, FinancialTransationCreateAPIView, FinancialTransactionDestroyAPIView


urlpatterns = [

        path('financial-transaction/', FinancialTransactionListAPIView.as_view(), name='financial_transaction'),
        path('create-financial-transaction/', FinancialTransationCreateAPIView.as_view(), name='financial_transaction-create'),
        path('update-delete-financial-transaction/<int:pk>/', FinancialTransactionDestroyAPIView.as_view(), name='delete_financial_transaction'),
        ]
