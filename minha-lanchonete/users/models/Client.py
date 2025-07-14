from django.db import models
from .User import User

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    cpf = models.CharField(max_length=11, unique=True)
    address = models.TextField()