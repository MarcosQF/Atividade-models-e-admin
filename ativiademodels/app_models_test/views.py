from django.shortcuts import render
from .models import Suplier, Product, Category
from .forms import SuplierForm, CategoryForm, ProductForm

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

def suplier_create(request):
    if request.method == 'POST':
        form = SuplierForm(request.POST)
        if form.is_valid():
            form.save()
            form = SuplierForm()
    else:
        form = SuplierForm()
    return render(request, 'app_models_test/suplier_forms.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'app_models_test/category_forms.html', {'form': form})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'app_models_test/product_forms.html', {'form': form})