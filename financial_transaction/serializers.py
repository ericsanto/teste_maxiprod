from rest_framework import serializers
from .models import FinancialTransaction


class FinancialTransactionModelSerializer(serializers.ModelSerializer):
    expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model = FinancialTransaction
        fields = ['id', 'methods_payment', 'expenses_category', 'expense', 'date', 'description', 'type_expense']  # Sem o campo "user"
        read_only_fields = ['user']
    
    """atribui o id do usuário logado ao campo 'user'. Para que não precise ser passado
    no corpo da requisição"""
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
