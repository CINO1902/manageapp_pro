from drf_yasg.utils import swagger_auto_schema

from .models import Attendance, FIRST_COUNTING, SECOND_COUNTING
from .serializers import (
    AttendanceSerializer,
    AttendanceCreateSerializer,
    AttendanceUpdateSerializer,
    DashboardSerializer,
)
from .filters import AttendanceFilter

from rest_framework import viewsets, status, serializers, generics
from rest_framework.response import Response

from rest_framework.exceptions import PermissionDenied

from ..utils.clean import clean_attendance_save
from ..utils.permissions import IsStaff
from django.db.models import Q, QuerySet
from datetime import datetime, timedelta


# class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A viewset for viewing dashboard content.
#     """
#
#     serializer_class = DashboardSerializer
#     queryset = Attendance.objects.all()


class AttendanceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing attendance instances.
    """

    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.filter(created_date__gte=(datetime.today() - timedelta(days=90)))
    filterset_class = AttendanceFilter

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Attendance.objects.select_related(
                "event", "counter", "count_coordinator"
            ).all()

        return Attendance.objects.select_related(
            "event", "counter", "count_coordinator"
        ).filter(Q(counter=current_user) | Q(count_coordinator=current_user))

    @swagger_auto_schema(
        request_body=AttendanceCreateSerializer(),
        responses={status.HTTP_201_CREATED: AttendanceSerializer()},
    )
    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied(detail="Permission denied")
        serializer = AttendanceCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            AttendanceSerializer(instance=self.obj).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @swagger_auto_schema(
        request_body=AttendanceUpdateSerializer(),
        responses={status.HTTP_200_OK: AttendanceSerializer()},
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance: Attendance = self.get_object()
        self.obj_instance = instance
        if (
            not request.user.is_superuser
            and request.user != instance.counter
            and request.user != instance.count_coordinator
        ):
            raise PermissionDenied(detail="Permission denied")
        serializer = AttendanceUpdateSerializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(
            AttendanceSerializer(instance=self.obj).data,
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        self.obj = serializer.save(counting_done=True)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        allocated_row = validated_data.get("allocated_row")
        service_index = validated_data.get("service_index")
        counter = validated_data.get("counter")
        event = validated_data.get("event")

        clean_attendance_save(
            exception_class=serializers.ValidationError,
            allocated_row=allocated_row,
            service_index=service_index,
            counter=counter,
            event=event,
        )

        self.obj = serializer.save(
            count_coordinator=self.request.user, counting_index=FIRST_COUNTING
        )

        if event.double_counting:
            serializer.save(
                count_coordinator=self.request.user, counting_index=SECOND_COUNTING
            )
