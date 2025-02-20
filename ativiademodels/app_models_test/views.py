from django.shortcuts import render
from .models import Suplier, Product, Category
from .forms import SuplierForm, CategoryForm, ProductForm
from django.views.generic import ListView,CreateView,TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(TemplateView):
  template_name = 'app_models_test/index.html'
    

# Supliers Views
class SupliersListView(ListView):
  model = Suplier
  template_name = 'app_models_test/supliers.html'
  context_object_name = 'supliers'
  
class SuplierCreate(CreateView):
    template_name= "app_models_test/suplier_forms.html"
    model = Suplier
    form_class = SuplierForm
    success_url = reverse_lazy("suplier_list")

#Category Views
class CategoryListView(ListView):
  model = Category
  template_name = 'app_models_test/category.html'
  context_object_name = 'category'

class CategoryCreate(CreateView):
    template_name= "app_models_test/category_forms.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

#Product Views
class ProductCreate(CreateView):
    template_name= "app_models_test/product_forms.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):

        response = super().form_valid(form)
        messages.success(self.request, "Produto criado com sucesso!")
        return response


class ProductsListView(ListView):
  model = Product
  template_name = 'app_models_test/products.html'
  context_object_name = 'products'
  paginate_by = 5

  def get_queryset(self) :
        queryset = super().get_queryset()
        nome = self.request.GET.get("nome")
        preco_min = self.request.GET.get("preco_min")
        preco_max = self.request.GET.get("preco_max")

        if nome:
            queryset = queryset.filter(product_name__icontains=nome)

        if preco_min:
            queryset = queryset.filter(price__gte=preco_min)

        if preco_max:
            queryset = queryset.filter(price__lte=preco_max)

        return queryset


