from django.urls import path
from rest_framework import routers

from .views import CustomUserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

router = routers.SimpleRouter()
router.register(r"customusers", CustomUserViewSet)


urlpatterns = [
    path("auth/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
