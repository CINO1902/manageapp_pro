from django.contrib import admin

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
