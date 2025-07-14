from django.db import models
from .User import User

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")
    pis_pasep = models.CharField(max_length=10, unique=True)
    admission_at = models.DateTimeField(auto_now_add=True)
    