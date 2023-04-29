import django_filters
from django.db.models import Count

from .models import Attendance


class AttendanceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    event__id = django_filters.CharFilter(lookup_expr="iexact")
    counter__id = django_filters.CharFilter(lookup_expr="iexact")
    count_coordinator__id = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Attendance
        fields = ["name", "event__id", "counter__id", "count_coordinator__id"]


# class CourseFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
#     code = django_filters.CharFilter(field_name="code", lookup_expr="icontains")
#     department__id = django_filters.CharFilter(lookup_expr="iexact")
#     popular = django_filters.BooleanFilter(method="filter_popular")
#
# def filter_popular(self, queryset, name, value):
#     if value is not None and value:
#         no_of_user = queryset.filter(counting_done=True).annotate(no_of_count_done=Count("counting_done")).order_by(
#             "-no_of_count_done"
#         )[:10]
#         return no_of_user
#     return queryset
#
#     class Meta:
#         model = Course
#         fields = ["title", "code", "department__id", "popular"]
