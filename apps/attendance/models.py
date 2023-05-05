from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError

# from rest_framework.serializers import ValidationError

FIRST_COUNTING = "FIRST_COUNTING"
SECOND_COUNTING = "SECOND_COUNTING"

COUNTING_INDEX = (
    (FIRST_COUNTING, FIRST_COUNTING),
    (SECOND_COUNTING, SECOND_COUNTING),
)


class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    allocated_row = models.PositiveIntegerField()

    service_index = models.PositiveIntegerField(verbose_name="Service No")

    adult_male_count = models.PositiveIntegerField(
        default=0,
    )

    adult_female_count = models.PositiveIntegerField(
        default=0,
    )

    teenager_male_count = models.PositiveIntegerField(
        default=0,
    )

    teenager_female_count = models.PositiveIntegerField(
        default=0,
    )

    children_male_count = models.PositiveIntegerField(
        default=0,
    )

    children_female_count = models.PositiveIntegerField(
        default=0,
    )

    male_first_timer_count = models.PositiveIntegerField(
        default=0,
    )

    female_first_timer_count = models.PositiveIntegerField(
        default=0,
    )

    adult_coverts_count = models.PositiveIntegerField(
        default=0,
    )

    teenager_coverts_count = models.PositiveIntegerField(
        default=0,
    )

    vehicle_count = models.PositiveIntegerField(
        default=0,
    )

    motor_bikes_count = models.PositiveIntegerField(
        default=0,
    )

    counting_done = models.BooleanField(default=False)

    event = models.ForeignKey(
        to="service.Event",
        on_delete=models.CASCADE,
    )

    counting_index = models.CharField(
        max_length=250, choices=COUNTING_INDEX, default=FIRST_COUNTING
    )

    counter = models.ForeignKey(
        related_name="counter",
        to="authentication.CustomUser",
        on_delete=models.CASCADE,
    )

    count_coordinator = models.ForeignKey(
        related_name="count_coordinator",
        limit_choices_to={"is_staff": True},
        to="authentication.CustomUser",
        on_delete=models.CASCADE,
    )

    updated_date = models.DateTimeField(
        auto_now=True,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Attendance"

        verbose_name_plural = "Attendances"

        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.id}"

    def clean(self):
        # pass
        # event = self.event
        from ..utils.clean import clean_attendance_save

        if not self.id:
            clean_attendance_save(
                exception_class=ValidationError,
                allocated_row=self.allocated_row,
                service_index=self.service_index,
                counter=self.counter,
                event=self.event,
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Attendance, self).save(*args, **kwargs)

    def total_attendance_count(self):
        return (
            self.adult_male_count
            + self.adult_female_count
            + self.teenager_male_count
            + self.teenager_female_count
            + self.children_male_count
            + self.children_female_count
            + self.male_first_timer_count
            + self.female_first_timer_count
            + self.adult_coverts_count
            + self.teenager_coverts_count
            + self.vehicle_count
            + self.motor_bikes_count
        )
