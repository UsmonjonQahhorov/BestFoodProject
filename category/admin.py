from django.contrib import admin

from category.models import Category


# @admin.action(description="Set selected category active.")
# def set_active(modeladmin, request, queryset):
#     (queryset.update(is_active=True))


@admin.display(description="Category Name")
def category_name(obj):
    return f"{obj.name}"


# @admin.action(description="Set selected categoty disactive.")
# def set_disactive(modeladmin, request, queryset):
#     (queryset.update(is_active=False))


class CategoryAdmin(admin.ModelAdmin):
    # actions = [set_active, set_disactive]
    list_display = [category_name, 'name']
    list_display_links = [category_name]  # Link to the 'food_name' field
    search_fields = ["name"]
    ordering = ["-created_at", "-updated_at"]


admin.site.register(Category, CategoryAdmin)
