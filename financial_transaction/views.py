from django.shortcuts import get_object_or_404
from rest_framework.exceptions import status
from rest_framework.mixins import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
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
    
    def post(self, request, *args, **kwargs):
        if int(self.request.user.age) < 18 and request.data.get('type_expense') == 'RECEITA':
            return Response({"detail": "Método receita é permitido somente para pessoas acima de 18 anos!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)

class FinancialTransactionDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialTransactionModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        get_financial = FinancialTransaction.objects.filter(user=self.request.user.id)
        print(get_financial)
        return get_financial



