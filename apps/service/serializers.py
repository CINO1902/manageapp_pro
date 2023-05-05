from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers


from .models import Event

from .models import ServiceType

from .models import ServiceUnit


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"

    def create(self, validated_data):
        servicetype = ServiceType.objects.create(**validated_data)
        return servicetype

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class EventSerializer(serializers.ModelSerializer):
    from ..attendance.serializers import AttendanceSerializer

    all_event_attendance_count = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    service_type_obj = ServiceTypeSerializer(read_only=True, source="service_type")
    attendance_set = AttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("service_type_obj",)

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    @swagger_serializer_method(serializers.IntegerField)
    def get_all_event_attendance_count(self, instance: Event):
        return instance.all_event_attendance_count()

    @swagger_serializer_method(serializers.CharField)
    def get_name(self, instance: Event):
        return instance.get_event_name()


class ServiceUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUnit
        fields = "__all__"

    def create(self, validated_data):
        serviceunit = ServiceUnit.objects.create(**validated_data)
        return serviceunit

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
