from rest_framework import serializers
from minha_lanchonete.models.Pizza import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    
    class Meta:
        model = Pizza
        fields = ("id", "name", "value", "size", "description")
        
    def get_id(self, obj):
        return obj.product.id
        
    def get_name(self, obj):
        return obj.product.name
    
    def get_value(self, obj):
        return obj.product.value