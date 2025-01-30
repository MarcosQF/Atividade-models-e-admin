from xml.dom import ValidationErr
from django import forms
from .models import Product, Category, Suplier
from django.core.validators import RegexValidator

class SuplierForm(forms.ModelForm):
    class Meta:
        model = Suplier
        fields = ['suplier_name', 'cnpj']
        widgets = {
            'cnpj': forms.TextInput(attrs={'maxlength': 14}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['suplier', 'categories', 'product_name', 'product_code', 'description', 'price', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
        }

    suplier = forms.ModelChoiceField(queryset=Suplier.objects.all(), empty_label="Selecione um fornecedor")
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

   