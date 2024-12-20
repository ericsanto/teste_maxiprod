from django.db import models
from django.contrib.auth.models import User
from django.utils import choices
from django.utils.regex_helper import Choice
from authentication.models import UserCustom

EXPENSE_CATEGORIES = (
        ('ACADEMIA', 'ACADEMIA'),
        ('SAÚDE', 'SAÚDE'),
        ('SALÃO DE BELEZA', 'SALÃO DE BELEZA'),
        ('ALIMENTAÇÃO', 'ALIMENTAÇÃO'),
        ('ROUPAS', 'ROUPAS'),
        ('CAMA MESA E BANHO', 'CAMA, MESA E BANHO'),
        ('ELETRODOMÉSTICO', 'ELETRODOMÉSTICO'),
        ('CONTA DE ÁGUA', 'CONTA DE ÁGUA'),
        ('CONTA DE LUZ', 'CONTA DE LUZ'),
        ('ALUGUEL', 'ALUGUEL')
        )

MATHODS_PAYMENT = (
        ('DINHEIRO', 'DINHEIRO'),
        ('CARTÃO', 'CARTÃO'),
        ('', '')
        )


TYPE_EXPENSE = (
        ('DESPESA', 'DESPESA'),
        ('RECEITA', 'RECEITA'),
        )

class FinancialTransaction(models.Model):
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE, blank=True, related_name='transactions')
    methods_payment = models.CharField(choices=MATHODS_PAYMENT, max_length=255)
    expenses_category = models.CharField(choices=EXPENSE_CATEGORIES, max_length=255, blank=True)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    type_expense = models.CharField(choices=TYPE_EXPENSE, max_length=255)

