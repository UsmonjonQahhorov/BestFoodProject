from django.contrib import admin
from orderfood.models import Food, Order, OrderFood


@admin.action(description="Set selected food active.")
def set_active(modeladmin, request, queryset):
    (queryset.update(is_active=True))


@admin.display(description="Food Name")
def food_name(obj):
    return f"{obj.name}"


@admin.action(description="Set selected food disactive.")
def set_disactive(modeladmin, request, queryset):
    (queryset.update(is_active=False))


class FoodAdmin(admin.ModelAdmin):
    actions = [set_active, set_disactive]
    list_display = [food_name, 'price', 'is_active', 'category']  # Include 'food_name'
    list_display_links = [food_name]  # Link to the 'food_name' field
    search_fields = ["name", 'description', 'category']
    list_filter = ['category', 'price']
    ordering = ["-created_at", "-updated_at"]
    fieldsets = [
        (
            "MAIN INFO",
            {
                "fields": ["name", "price"]
            }
        ),
        (
            "Extra Information",
            {
                "fields": ["description", "is_active", "image"]
            }
        ),
        (
            "Category",
            {
                "fields": ["category"]
            }
        )
    ]


@admin.display(description="order_price")
def order_price(obj):
    return f"{obj.total_price}"


class OrderAdmin(admin.ModelAdmin):
    list_display = [order_price, 'telegram_user', 'delivered_by', 'status', 'delivered_at']
    list_display_links = [order_price]  # Link to the 'order_price' field
    search_fields = ["total_price", 'delivered_by', 'delivered_at']
    list_filter = ['status', 'delivered_by']
    ordering = ["-created_at", "-updated_at"]
    fieldsets = [
        (
            "MAIN INFO",
            {
                "fields": ["total_price", "telegram_user", "status"]
            }
        ),
        (
            "Extra Information",
            {
                "fields": ["description", "lon", "lat"]
            }
        ),
        (
            "Other Info",
            {
                "fields": ["delivered_by"]
            }
        )
    ]


admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
