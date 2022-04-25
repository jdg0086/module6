from django import forms

from .models import Branch, Agent, Transaction


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['location_name']
        labels = {'location_name': 'Branch Location'}


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'special_license']
        labels = {'name': 'Name', 'special_license': 'Has Special License'}


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['buyer_name', 'volume', 'gross_sale_amount', 'order_number']
        labels = {'buyer_name': 'Buyer Name',
                  'volume': 'Volume',
                  'gross_sale_amount': 'Dollar Amount',
                  'order_number': 'Order Number'
                  }

