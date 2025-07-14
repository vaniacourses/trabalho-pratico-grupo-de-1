from django.db import models
from users.models.Client import Client

class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=12, unique=True)
    
    def __str__(self):
        return str(self.number)
    
    class Meta:
        db_table = 'payment_method'
        managed = True
        verbose_name = 'PaymentMethod'
        verbose_name_plural = 'PaymentMethods'
        unique_together = ("client", "number")
        ordering = ["-id"]