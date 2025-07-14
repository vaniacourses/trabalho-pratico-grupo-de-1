from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Order, OrderProduct, PaymentMethod, Product
from minha_lanchonete.serializers import OrderSerializer, OrderWithProductsSerializer

from users.helpers import UserHelper


class OrderView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        if(UserHelper.is_admin(request.user)):
            orders = Order.objects.all()
            return Response(data=OrderWithProductsSerializer(orders, many=True).data)
        elif(UserHelper.is_client(request.user)):
            orders = Order.objects.filter(client=request.user.client)
            return Response(data=OrderWithProductsSerializer(orders, many=True).data)
        else:
            return Response(status=500)
    
    def update(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        instance.status = request.data['status']
        instance.save()
        return Response(data=OrderWithProductsSerializer(instance, many=False).data)
    
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_client(request.user)):
           return Response(status=403) 
        payment_method = PaymentMethod.objects.get(id=request.data['payment_method'])
        if(payment_method.client != request.user.client):
            return Response(status=403)
        order = Order.objects.create(payment_method=payment_method, client=request.user.client)
        order.save()
        for product in request.data['products']:
            p = Product.objects.get(id=product)
            order_product = OrderProduct.objects.create(order=order, product=p)
            order_product.save()
        return Response(data=OrderWithProductsSerializer(order, many=False).data)