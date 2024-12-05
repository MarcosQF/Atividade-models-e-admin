from django.db import models

class Product(models.Model):
   product_name = models.CharField('Nome',max_length = 200, blank = False)
   product_code = models.CharField('Codigo',max_length = 200, blank = False, unique = True)
   description = models.TextField('Descricao ', blank = True)
   price = models.DecimalField('Preco',max_digits=10, decimal_places=2)
   quantity = models.IntegerField('Quantidade')
   pub_date = models.DateTimeField('data de criacao',auto_now_add=True)



