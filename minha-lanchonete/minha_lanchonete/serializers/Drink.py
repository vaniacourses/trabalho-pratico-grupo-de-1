from rest_framework import serializers
from minha_lanchonete.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    
    class Meta:
        model = Drink
        fields = ("id", "name", "value", "volume", "type")
        
    def get_id(self, obj):
        return obj.product.id
        
    def get_name(self, obj):
        return obj.product.name
    
    def get_value(self, obj):
        return obj.product.value