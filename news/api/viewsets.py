from rest_framework import viewsets

from news.models import News
from news.api.serializers import NewsSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer