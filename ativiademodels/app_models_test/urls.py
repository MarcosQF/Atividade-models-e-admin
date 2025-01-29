from django.urls import path, include
from . import views


urlpatterns = [
    path('supliers/list', views.supliers),
    path('products/list', views.products), 
    path('categories/list', views.category),

    path('supliers/create/', views.suplier_create, name='suplier_create'),
    path('categories/create/', views.category_create, name='category_create'),
    path('products/create/', views.product_create, name='product_create'),
]