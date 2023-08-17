from django.db import models

from category.models import Category
from users.models import TgUser
from users.models import User


class StatusChoices(models.TextChoices):
    PREPARING = ("preparing", "Preparing")
    DELIVERING = ("delivering", "Delivering")
    DELIVERED = ("delivered", "Delivered")


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    category = models.ForeignKey(Category,related_name="category-food",on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Foods"
        verbose_name_plural = "Foods"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"




class Order(models.Model):
    total_price = models.FloatField()
    lat = models.DecimalField()
    lon = models.DecimalField()
    description = models.TextField()
    telegram_user = models.ForeignKey(TgUser,related_name="order-telegram-user",on_delete=models.CASCADE)
    delivered_by = models.ForeignKey(User,related_name="order-delivered",on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=StatusChoices.choices)
    delivered_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.description}"




class OrderFood(models.Model):
    order  = models.ForeignKey(Order, related_name="orderfood-order",on_delete=models.CASCADE)
    food  = models.ForeignKey(Food, related_name="orderfood-food",on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
