from django.urls import path, include
from . import views


urlpatterns = [
    path('supliers/list', views.SupliersListView.as_view(),name='suplier_list'),
    path('products/list', views.ProductsListView.as_view(),name='product_list'), 
    path('categories/list', views.CategoryListView.as_view(),name='category_list'),

    path('supliers/create/', views.SuplierCreate.as_view(), name='suplier_create'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
]