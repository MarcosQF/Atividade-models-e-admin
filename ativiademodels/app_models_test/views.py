from django.shortcuts import render
from .models import Suplier, Product, Category
from .forms import SuplierForm, CategoryForm, ProductForm
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
# Create your views here.

class SupliersListView(ListView):
  model = Suplier
  template_name = 'app_models_test/supliers.html'
  context_object_name = 'supliers'

class ProductsListView(ListView):
  model = Product
  template_name = 'app_models_test/products.html'
  context_object_name = 'products'

class CategoryListView(ListView):
  model = Category
  template_name = 'app_models_test/category.html'
  context_object_name = 'category'

class SuplierCreate(CreateView):
    template_name= "app_models_test/suplier_forms.html"
    model = Suplier
    form_class = SuplierForm
    success_url = reverse_lazy("suplier_list")
    
class CategoryCreate(CreateView):
    template_name= "app_models_test/category_forms.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

class ProductCreate(CreateView):
    template_name= "app_models_test/product_forms.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

