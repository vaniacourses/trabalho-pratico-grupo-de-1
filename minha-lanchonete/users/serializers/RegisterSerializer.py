from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import models

from users.models import User, Client

class RegisterSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=True)
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message="Já existe um usuário cadastrado com esse e-mail.", lookup='iexact')]
            )
    phone = serializers.CharField(required=True)
    
    password = serializers.CharField(write_only=True, required=True)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        name = validated_data.pop("name")
        email = validated_data.pop("email")
        phone = validated_data.pop("phone")
        user = User.objects.create(name=name, email=email, phone=phone)
        user.set_password(password)
        user.save()
        client = Client.objects.create(**validated_data, user=user)
        client.save()
        return user
    
    class Meta:
        model = Client
        fields = ("password", "name", "email", "phone", "cpf", "address")