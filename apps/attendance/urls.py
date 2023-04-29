from rest_framework import routers

from .views import AttendanceViewSet

router = routers.SimpleRouter()

router.register(r"attendances", AttendanceViewSet)
# router.register(r"dashboard", DashboardViewSet)

urlpatterns = router.urls
