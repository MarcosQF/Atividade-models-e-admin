from django.shortcuts import render
from .models import Suplier, Product, Category

# Create your views here.

def supliers(request):
    supliers = Suplier.objects.all()
    context = {'supliers': supliers}
    return render(request, 'app_models_test/supliers.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app_models_test/products.html', context)

def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'app_models_test/category.html',context)