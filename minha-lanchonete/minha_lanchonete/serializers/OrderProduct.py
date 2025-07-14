from rest_framework import serializers
from minha_lanchonete.models import OrderProduct
from minha_lanchonete.serializers.Order import OrderSerializer
from minha_lanchonete.serializers.Product import ProductSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    
    order = OrderSerializer(many=False)
    product = ProductSerializer(many=False)
    
    class Meta:
        model = OrderProduct
        fields = ("id", "order", "product")