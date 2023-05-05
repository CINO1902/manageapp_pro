from ..attendance.models import Attendance
from .serializers import EventSerializer

from .models import ServiceType
from .serializers import ServiceTypeSerializer

from .models import ServiceUnit, Event
from .serializers import ServiceUnitSerializer

from rest_framework import viewsets
from .filters import EventFilter, ServiceTypeFilter, ServiceUnitFilter
from django.db.models import Q, QuerySet
from datetime import datetime, timedelta

class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """

    serializer_class = EventSerializer
    filterset_class = EventFilter
    queryset = Event.objects.filter(created_date__gte=(datetime.today() - timedelta(days=90))) # records of 3months

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Event.objects.all()

        return Event.objects.filter(
            pk__in=Attendance.objects.select_related(
                "event", "counter", "count_coordinator"
            )
            .filter(Q(counter=current_user) | Q(count_coordinator=current_user))
            .values_list("event", flat=True)
        )


class ServiceTypeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing servicetype instances.
    """

    serializer_class = ServiceTypeSerializer
    filterset_class = ServiceTypeFilter
    queryset = ServiceType.objects.all()


class ServiceUnitViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing serviceunit instances.
    """

    serializer_class = ServiceUnitSerializer
    filterset_class = ServiceUnitFilter
    queryset = ServiceUnit.objects.all()
