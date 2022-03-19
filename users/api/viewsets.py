from rest_framework import viewsets

from users.models import User
from users.api.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer