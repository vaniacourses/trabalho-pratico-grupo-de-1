from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from users.serializers.UserSerializer import UserAdminSerializer, UserClientSerializer

from users.helpers import UserHelper

class LoginSerializer(TokenObtainPairSerializer):
    
    @classmethod 
    def get_token(cls, user):
        return super().get_token(user)
    
    
    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(email=self.user)
        serializer = None
        if UserHelper.is_admin(user):
            serializer = UserAdminSerializer(user)
        else:
            serializer = UserClientSerializer(user)
        data["user"] = serializer.data
        return data