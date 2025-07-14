from rest_framework import serializers
from minha_lanchonete.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "value")

class PizzaProductSerializer(serializers.ModelSerializer):
    
    size = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ("id", "name", "value", "size", "description")
        
    def get_size(self, obj):
        return obj.pizza.size
    
    def get_description(self, obj):
        return obj.pizza.description

class DrinkProductSerializer(serializers.ModelSerializer):
    
    volume = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ("id", "name", "value", "volume", "type")
        
    def get_volume(self, obj):
        return obj.drink.volume

    def get_type(self, obj):
        return obj.drink.type