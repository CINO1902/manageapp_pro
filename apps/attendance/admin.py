from datetime import datetime
from django.contrib import admin
# from rangefilter.filters import (
#     DateRangeFilterBuilder,
#     DateTimeRangeFilterBuilder,
#     NumericRangeFilterBuilder,
# )

from .models import Attendance


# admin.site.register(Attendance)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """Admin View for Attendance"""

    list_display = (
        "id",
        "service_index",
        "allocated_row",
        "counter",
        "count_coordinator",
    )

    # list_filter = (
    #     (
    #         "created_date",
    #         DateTimeRangeFilterBuilder(
    #             title="Search",
    #             default_start=datetime.now(),
    #         ),
    #     ),
    # )
