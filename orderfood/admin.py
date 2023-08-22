from django.contrib import admin

from orderfood.models import Order, Food, OrderFood

admin.site.register(Order)
admin.site.register(Food)
admin.site.register(OrderFood)