from django.db.models import Count
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from .models import Attendance
from ..service.models import Event

from ..authentication.serializers import CustomUserSerializer


from ..authentication.models import CustomUser


class AttendanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = (
            "service_index",
            "allocated_row",
            "event",
            "counter",
        )

    def create(self, validated_data):
        print("First Time | Second Time")
        attendance = Attendance.objects.create(**validated_data)
        return attendance


class AttendanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = (
            "adult_male_count",
            "adult_female_count",
            "teenager_male_count",
            "teenager_female_count",
            "children_male_count",
            "children_female_count",
            "male_first_timer_count",
            "female_first_timer_count",
            "adult_coverts_count",
            "teenager_coverts_count",
            "vehicle_count",
            "motor_bikes_count",
        )

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class AttendanceSerializer(serializers.ModelSerializer):
    total_attendance_count = serializers.SerializerMethodField()
    counter_name = serializers.SerializerMethodField()
    coordinator_name = serializers.SerializerMethodField()
    event_name = serializers.SerializerMethodField()
    event_is_locked = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = "__all__"

    @swagger_serializer_method(serializers.IntegerField)
    def get_total_attendance_count(self, instance: Attendance) -> str:
        return instance.total_attendance_count()

    @swagger_serializer_method(serializers.CharField)
    def get_counter_name(self, instance: Attendance):
        return instance.counter.get_full_name()

    @swagger_serializer_method(serializers.CharField)
    def get_event_name(self, instance: Attendance):
        return instance.event.name
    
    @swagger_serializer_method(serializers.BooleanField)
    def get_event_is_locked(self, instance: Attendance) -> bool:
        return instance.event.is_locked

    @swagger_serializer_method(serializers.CharField)
    def get_coordinator_name(self, instance: Attendance) -> str:
        return instance.count_coordinator.get_full_name()



class DashboardSerializer(serializers.ModelSerializer):
    total_event = serializers.SerializerMethodField()
    total_users = serializers.SerializerMethodField()
    top_events = serializers.SerializerMethodField()
    top_ushers = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ["id", "total_event", "total_users", "top_events", "top_ushers"]

    @swagger_serializer_method(serializers.IntegerField)
    def get_total_event(self, instance: Attendance) -> str:
        return Event.objects.count()

    # @swagger_serializer_method(EventSerializer)
    def get_top_events(self, instance: Attendance) -> str:
        from ..service.serializers import EventSerializer

        events = Event.objects.filter(
            pk__in=Attendance.objects.all()
            .annotate(top_event=Count("event"))
            .order_by("-top_event")[:5]
            .values_list("event", flat=True)
        ).values_list("name", flat=True)
        return events

    @swagger_serializer_method(serializers.IntegerField)
    def get_total_users(self, instance: Attendance) -> str:
        return CustomUser.objects.count()

    @swagger_serializer_method(serializers.IntegerField)
    def get_top_ushers(self, instances: Attendance) -> str:
        ushers = CustomUser.objects.filter(
            pk__in=Attendance.objects.all()
            .annotate(top_ushers=Count("counter"))
            .order_by("-top_ushers")[:5]
            .values_list("counter", flat=True)
        ).values_list("first_name", "last_name")
        return ushers
