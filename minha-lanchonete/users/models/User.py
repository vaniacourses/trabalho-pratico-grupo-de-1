from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    
    
    @property
    def cpf(self):
        return self.client.cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.client.cpf = cpf
        self.client.save()
    
    @property
    def address(self):
        return self.client.address
    
    @address.setter
    def address(self, address):
        self.client.address = address
        self.client.save()

    @property
    def pis_pasep(self):
        return self.admin.pis_pasep
    
    @pis_pasep.setter
    def pis_pasep(self, pis_pasep):
        self.admin.pis_pasep = pis_pasep
        self.admin.save()
        
    @property
    def admission_at(self):
        return self.admin.admission_at
    
    @admission_at.setter
    def admission_at(self, admission_at):
        self.admin.admission_at
        self.admin.save()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []