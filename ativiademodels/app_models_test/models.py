from django.db import models

class Product(models.Model):
   suplier = models.ForeignKey('Suplier', on_delete=models.CASCADE)
   categories = models.ManyToManyField('Category', related_name='questions')
   
   product_name = models.CharField('Nome',max_length = 200, blank = False)
   product_code = models.CharField('Codigo',max_length = 200, blank = False, unique = True)
   description = models.TextField('Descricao ', blank = True)
   price = models.DecimalField('Preco',max_digits=10, decimal_places=2)
   quantity = models.IntegerField('Quantidade')
   pub_date = models.DateTimeField('data de criacao',auto_now_add=True)
   
   def __str__(self):
       return self.product_name


class Category(models.Model):
   category_name = models.CharField('Nome', max_length = 200, blank = True)
   
   def __str__(self):
       return self.category_name
   

class Suplier(models.Model):
   suplier_name = models.CharField('Nome', max_length = 200, blank = True)
   cnpj = models.CharField('CNPJ', max_length = 14, blank = False)
   def __str__(self):
       return self.suplier_name



