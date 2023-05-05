from django.core.exceptions import ValidationError as CoreException
from rest_framework.serializers import ValidationError
from typing import Union

from apps.authentication.models import CustomUser
from apps.service.models import Event
from apps.attendance.models import Attendance


def clean_attendance_save(
    exception_class: Union[ValidationError, CoreException],
    allocated_row: int,
    service_index: int,
    counter: CustomUser,
    event: Event,
):
    if event:
        if (
            allocated_row is None
            or allocated_row < 1
            or allocated_row > event.total_seating_rows
        ):
            raise exception_class(
                {
                    "allocated_row": f"Allocated rows should be between 1 and event's total seating rows ({event.total_seating_rows})"
                },
                code="invalid",
            )

        if (
            service_index is None
            or service_index < 1
            or service_index > event.total_service_count
        ):
            raise exception_class(
                {
                    "service_index": f"Allocated rows should be between 1 and event's total service count ({event.total_service_count})"
                },
                code="invalid",
            )

        has_error = True
        try:
            Attendance.objects.get(
                allocated_row=allocated_row,
                service_index=service_index,
                event=event,
            )
        except Attendance.DoesNotExist:
            has_error = False

        if has_error:
            raise exception_class(
                {
                    "event": f"A counter has already been allocated to this event at service index {service_index} and row {allocated_row}"
                },
                code="invalid",
            )

        has_error = True

        try:
            Attendance.objects.get(event=event, counter=counter)
        except Attendance.DoesNotExist:
            has_error = False

        if has_error:
            raise exception_class(
                {"counter": "This counter has already been allocated to this event"},
                code="invalid",
            )
