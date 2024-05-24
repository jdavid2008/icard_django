from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password']) # Encriptamos la contraseña
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        password = request.data.get('password', None)

        if password is not None:
            request.data['password']=make_password(password) # Encriptamos la contraseña
        
        return super().partial_update(request, *args, **kwargs)
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
  
    def get(self, request):
        seriealizer = UserSerializer(request.user)
        return Response(seriealizer.data)
    