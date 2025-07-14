from rest_framework import serializers
from minha_lanchonete.models import Order, OrderProduct
from minha_lanchonete.serializers.PaymentMethod import PaymentMethodSerializer
from minha_lanchonete.helpers import ProductHelper

from minha_lanchonete.serializers.Product import PizzaProductSerializer, DrinkProductSerializer
from users.serializers import ClientSerializer

class OrderSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer(many=False)
    payment_method = PaymentMethodSerializer(many=False)
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "client", "payment_method", "status")
        
class OrderWithProductsSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer(many=False)
    payment_method = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "client", "payment_method", "products", "status")
    
    def get_payment_method(self, obj):
        return obj.payment_method.number
        
    def get_products(self, obj):
        order_products = OrderProduct.objects.filter(order=obj)
        products = []
        for order_product in order_products:
            product = order_product.product
            if(ProductHelper.is_drink(product)):    
                products.append(DrinkProductSerializer(product, many=False).data)
            if(ProductHelper.is_pizza(product)):
                products.append(PizzaProductSerializer(product, many=False).data)
        return products