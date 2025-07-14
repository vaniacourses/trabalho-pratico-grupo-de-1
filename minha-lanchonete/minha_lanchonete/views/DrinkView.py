from itertools import product
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Drink, Product
from minha_lanchonete.serializers import DrinkSerializer
from users.helpers import UserHelper

class DrinkView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return(Response(status=403))
        product = Product.objects.create(name=request.data['name'], picture=request.data['picture'], value=request.data['value'])
        product.save()
        drink = Drink.objects.create(product=product, volume=request.data['volume'], type=request.data['type'])
        drink.save()
        return Response(data=DrinkSerializer(drink, many=False).data)

    def list(self, request, *args, **kwargs):
        drinks = Drink.objects.all()
        return Response(DrinkSerializer(drinks, many=True).data)