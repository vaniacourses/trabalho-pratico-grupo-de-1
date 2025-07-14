from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.helpers import UserHelper
from users.models import User, Client, Admin
from users.serializers import ClientSerializer, UserSerializer, AdminSerializer

class UsersView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        clients = Client.objects.all()
        admins = Admin.objects.all()
        return Response(data={"clients": ClientSerializer(clients, many=True).data, "admins": AdminSerializer(admins, many=True).data})
        
    def destroy(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        instance.delete()
        return Response(status=200)