from itertools import product
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Pizza, Product
from minha_lanchonete.serializers import PizzaSerializer
from users.helpers import UserHelper

class PizzaView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return(Response(status=403))
        product = Product.objects.create(name=request.data['name'], picture=request.data['picture'], value=request.data['value'])
        product.save()
        pizza = Pizza.objects.create(product=product, size=request.data['size'], description=request.data['description'])
        pizza.save()
        return Response(data=PizzaSerializer(pizza, many=False).data)
    
    def list(self, request):
        pizzas = Pizza.objects.all()
        return Response(data=PizzaSerializer(pizzas, many=True).data)