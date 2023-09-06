from rest_framework import serializers
from orderfood.models import Order, Food


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
