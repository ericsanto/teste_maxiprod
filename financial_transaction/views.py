from .models import FinancialTransaction
from .serializers import FinancialTransactionModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
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


