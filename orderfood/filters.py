from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend


class OrderFoodIsActiveFitler(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_active = request.query_params.get("is_active")
        if is_active == "1":
            queryset = queryset.filter(is_active=True)
        elif is_active == "0":
            queryset = queryset.filter(is_active=False)
        return queryset


class OrderFoodStatusFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
