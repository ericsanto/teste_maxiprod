from django.urls import path
from .views import FinancialTransactionListAPIView, FinancialTransationCreateAPIView


urlpatterns = [

        path('financial-transaction/', FinancialTransactionListAPIView.as_view(), name='financial_transaction'),
        path('create-financial-transaction/', FinancialTransationCreateAPIView.as_view(), name='financial_transaction-create'),
        ]
