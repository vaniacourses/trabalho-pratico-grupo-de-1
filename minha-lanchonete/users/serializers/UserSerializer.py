from rest_framework import serializers

from users.models import User, Client, Admin

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email")

class AdminSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    
    class Meta:
        model = Admin
        fields = ("id", "name", "phone", "email", "pis_pasep", "admission_at")
    
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_phone(self, obj):
        return obj.user.phone
        
class ClientSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = ("id", "name", "phone", "email", "cpf", "address")
        
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_phone(self, obj):
        return obj.user.phone

class UserAdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email", "pis_pasep", "admission_at")
        
class UserClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email", "cpf", "address")