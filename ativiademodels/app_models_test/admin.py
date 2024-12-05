from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
   list_display = ['product_code', 'product_name','price','quantity','pub_date'] #listagem de atributos
   list_filter = ['pub_date'] #atributos a serem utilizados como filtros
   search_fields = ['product_name', 'product_code'] #atributos a serem utilizados em buscas
   ordering = ['-pub_date'] #ordenação a partir de um atributo

admin.site.register(Product,ProductAdmin)