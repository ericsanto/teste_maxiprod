from django.shortcuts import get_object_or_404
from .models import FinancialTransaction
from .serializers import FinancialTransactionModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class FinancialTransactionListAPIView(ListAPIView):
    serializer_class = FinancialTransactionModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):      
        financial_user = FinancialTransaction.objects.filter(user=self.request.user.id)
        return financial_user

class FinancialTransationCreateAPIView(CreateAPIView):
    serializer_class = FinancialTransactionModelSerializer
    permission_classes = [IsAuthenticated]


class FinancialTransactionDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialTransactionModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        get_financial = FinancialTransaction.objects.filter(user=self.request.user.id)
        print(get_financial)
        return get_financial



