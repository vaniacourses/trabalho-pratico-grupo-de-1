from rest_framework import serializers
from minha_lanchonete.models import PaymentMethod
from users.serializers.UserSerializer import ClientSerializer

class PaymentMethodSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer(many=False)
    
    class Meta:
        model = PaymentMethod
        fields = ("id", "number", "client")