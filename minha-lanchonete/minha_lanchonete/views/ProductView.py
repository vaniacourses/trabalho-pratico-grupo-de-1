from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Product, Drink, Pizza
from minha_lanchonete.serializers import DrinkSerializer, PizzaSerializer, ProductSerializer, PizzaProductSerializer, DrinkProductSerializer
from minha_lanchonete.helpers import ProductHelper
from users.helpers import UserHelper


class ProductView(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        drinks = Drink.objects.all()
        pizzas = Pizza.objects.all()
        return Response(data={"drinks": DrinkSerializer(drinks, many=True).data, "pizzas": PizzaSerializer(pizzas, many=True).data})
    
    def destroy(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        instance.delete()
        return Response(status=200)
    
    def update(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        if("name" in request.data):
            instance.name = request.data['name']
        if("picture" in request.data):
            instance.picture = request.data['picture']
        if("value" in request.data):
            instance.value = int(request.data['value'])
        if(ProductHelper.is_drink(instance)):
            if("volume" in request.data):
                instance.drink.volume = int(request.data['volume'])
            if("type" in request.data):
                instance.drink.type = request.data['type']
            instance.drink.save()
            instance.save()
            return Response(data=DrinkProductSerializer(instance, many=False).data)
        elif(ProductHelper.is_pizza(instance)):
            if("size" in request.data):
                instance.pizza.size = request.data['size']
            if("description" in request.data):
                instance.pizza.description = request.data['description']
            instance.pizza.save()
            instance.save()
            return Response(data=PizzaProductSerializer(instance, many=False).data)
        else:
            return Response(status=500)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if(ProductHelper.is_drink(instance)):
            return Response(data=DrinkProductSerializer(instance, many=False).data)
        elif(ProductHelper.is_pizza(instance)):
            return Response(data=PizzaProductSerializer(instance, many=False).data)
        else:
            return Response(status=500)