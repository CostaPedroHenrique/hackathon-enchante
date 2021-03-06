from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from news.views import TranslateView
from users.views import UserAuth, UserScoreView, UserView

from users.api.viewsets import UserViewset
from news.api.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'views', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/token/', UserAuth.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/', include(router.urls)),
    path('api/user/', UserView.as_view()),

    path('api/translate/', TranslateView.as_view()),

    path('api/score/', UserScoreView.as_view())
]
