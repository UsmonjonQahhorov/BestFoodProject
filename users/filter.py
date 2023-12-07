from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend

class UserRoleFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        role=request.query_params.get("role")
        if role:
            queryset=queryset.filter(role=role)
        return queryset

class TgUserIsBlockedFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_blocked=request.query_params.get("is_blocked")
        if is_blocked:
            queryset=queryset.filter(is_blocked=is_blocked)
        return queryset