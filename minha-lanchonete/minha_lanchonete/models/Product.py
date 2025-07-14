from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    picture = models.ImageField()
    value = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-id"]