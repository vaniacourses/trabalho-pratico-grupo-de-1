from django.db import models
from .PaymentMethod import PaymentMethod
from users.models.Client import Client

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    status = models.TextField(default="Pendente", null=False)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["-ordered_at"]