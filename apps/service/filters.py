import django_filters
from django.db.models import Count

from .models import Event, ServiceType, ServiceUnit


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    service_type__id = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Event
        fields = ["name", "service_type__name", "service_type__id"]


class ServiceTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ServiceType
        fields = ["name"]


class ServiceUnitFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ServiceUnit
        fields = ["name"]


# class CourseFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
#     code = django_filters.CharFilter(field_name="code", lookup_expr="icontains")
#     department__id = django_filters.CharFilter(lookup_expr="iexact")
#     popular = django_filters.BooleanFilter(method="filter_popular")
#
#     def filter_popular(self, queryset, name, value):
#         if value is not None and value:
#             no_of_user = queryset.annotate(no_of_user=Count("score")).order_by(
#                 "-no_of_user"
#             )[:10]
#             return no_of_user
#         return queryset
#
#     class Meta:
#         model = Course
#         fields = ["title", "code", "department__id", "popular"]
