from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import Admin, User
from users.serializers import UserSerializer, AdminSerializer
from users.helpers import UserHelper


class AdminsView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        user = User.objects.create(name=name, phone=phone, email=email)
        user.set_password(request.data['password'])
        user.save()
        pis_pasep = request.data['pis_pasep']
        admin = Admin.objects.create(user=user, pis_pasep=pis_pasep)
        admin.save()
        return Response(data=AdminSerializer(admin, many=False).data)
    
    def list(self, request, *args, **kwargs): 
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)  
        admins = Admin.objects.all()
        return Response(data=AdminSerializer(admins, many=True).data)
    