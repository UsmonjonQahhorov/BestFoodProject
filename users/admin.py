from django.contrib import admin
from orderfood.models import Food, Order, OrderFood
from users.models import User, TgUser


# @admin.action(description="Set selected user active.")
# def set_active(modeladmin, request, queryset):
#     return queryset.update(is_active=True)


@admin.display(description="User Name")
def first_name(obj):
    return f"{obj.firstname} {obj.lastname}"


# @admin.action(description="Set selected user disactive.")
# def set_disactive(modeladmin, request, queryset):
#     return queryset.update(is_active=False)


from users.models import User, TgUser
@admin.action(description="Send notification to selected users")
def send_notification(modeladmin, request, queryset):
    print("queryset", queryset)


class UserAdmin(admin.ModelAdmin):
    actions = [send_notification]
    list_display = [first_name, 'firstname', 'lastname', 'role']
    list_display_links = [first_name, 'firstname', 'role']
    search_fields = ["firstname", 'lastname', 'role']
    list_filter = ['firstname']
    ordering = ["-created_at", "-updated_at"]
    fieldsets = [
        (
            "MAIN INFO",
            {
                "fields": ["firstname", "lastname"]  # Include 'firstname'
            }
        ),
        (
            "Extra Information",
            {
                "fields": ["role"]
            }
        )
    ]


@admin.display(description="fullname")
def fullname(obj):
    return f"{obj.fullname}"


class TgUserAdmin(admin.ModelAdmin):
    list_display = [fullname, 'fullname', 'phone_number', 'is_blocked']
    list_display_links = [fullname]
    search_fields = ['fullname', 'phone_number']
    list_filter = ['is_blocked']
    ordering = ["-created_at", "-updated_at"]
    fieldsets = [
        (
            "MAIN INFO",
            {
                "fields": ["fullname", "phone_number"]
            }
        ),
        (
            "Extra Information",
            {
                "fields": ["is_blocked"]
            }
        )
    ]


admin.site.register(User, UserAdmin)
admin.site.register(TgUser, TgUserAdmin)

admin.site.register(User)
admin.site.register(TgUser)