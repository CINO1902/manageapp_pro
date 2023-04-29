from rest_framework import routers

from .views import EventViewSet

from .views import ServiceTypeViewSet

from .views import ServiceUnitViewSet

router = routers.SimpleRouter()

router.register(r"events", EventViewSet)

router.register(r"servicetypes", ServiceTypeViewSet)

router.register(r"serviceunits", ServiceUnitViewSet)

urlpatterns = router.urls
