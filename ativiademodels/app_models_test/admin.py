from django.contrib import admin

from .models import Product, Category, Suplier

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
   list_display = ['product_code', 'product_name','price','quantity','pub_date','suplier'] #listagem de atributos
   list_filter = ['pub_date'] #atributos a serem utilizados como filtros
   search_fields = ['product_name', 'product_code'] #atributos a serem utilizados em buscas
   ordering = ['-pub_date'] #ordenação a partir de um atributo

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['category_name'] #listagem de atributos
   list_filter = ['category_name'] #atributos a serem utilizados como filtros
   search_fields = ['category_name'] #atributos a serem utilizados em buscas

class SuplierAdmin(admin.ModelAdmin):
   list_display = ['suplier_name', 'cnpj'] #listagem de atributos
   list_filter = ['suplier_name'] #atributos a serem utilizados como filtros
   search_fields = ['suplier_name', 'cnpj'] #atributos a serem utilizados em buscas
   

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Suplier,SuplierAdmin)