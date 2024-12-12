from django.urls import path, include
from . import views


urlpatterns = [
    path('supliers/', views.supliers),
    path('products/', views.products), 
    path('category/', views.category)
]