from uuid import uuid4
from django.db import models

# from ..authentication.models import CustomUser

SUNDAY = "Sunday"
WEDNESDAY = "Wednesday"
COMMUNION_SERVICE = "Communion Service"
OTHER = "Other"

EVENT_NAME_CHOICE = (
    (SUNDAY, SUNDAY),
    (WEDNESDAY, WEDNESDAY),
    (COMMUNION_SERVICE, COMMUNION_SERVICE),
    (OTHER, OTHER),
)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=250, choices=EVENT_NAME_CHOICE, default=SUNDAY)

    other_name = models.CharField(max_length=250, blank=True, null=True)

    minister = models.CharField(max_length=50, blank=True, null=True)

    message = models.CharField(max_length=50, blank=True, null=True)

    service_type = models.ForeignKey(
        to="service.ServiceType",
        on_delete=models.CASCADE,
    )

    total_service_count = models.PositiveIntegerField(default=1)

    double_counting = models.BooleanField(default=False)

    total_seating_rows = models.PositiveIntegerField()

    duration = models.CharField(
        help_text="This is the service duration in format hr:min",
        max_length=200,
    )

    start_date = models.DateTimeField()

    updated_date = models.DateTimeField(
        auto_now=True,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    # allowed_counters = models.ManyToManyField(
    #     CustomUser, related_name="allowed_counters", blank=True
    # )

    class Meta:
        verbose_name = "Event"

        verbose_name_plural = "Events"

        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.name}"

    def all_event_attendance_count(self):
        event_attendances = self.attendance_set.all()
        total = 0
        for item in event_attendances:
            total += item.total_attendance_count()

        return total

    def get_event_name(self):
        if self.name == OTHER:
            return self.other_name

        return self.name


class ServiceType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(
        help_text="This is the name of the service type",
        max_length=200,
    )

    updated_date = models.DateTimeField(
        auto_now=True,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "ServiceType"

        verbose_name_plural = "ServiceTypes"

        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.name}"


class ServiceUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(
        help_text="This is the name of the unit",
        max_length=200,
    )

    updated_date = models.DateTimeField(
        auto_now=True,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.name}"
