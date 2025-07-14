from django.db import models
from .Product import Product

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1)
    description = models.TextField()
    
    def __str__(self):
        return str(self.product.name)
    
    class Meta:
        db_table = 'pizza'
        managed = True
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
        ordering = ["-id"]