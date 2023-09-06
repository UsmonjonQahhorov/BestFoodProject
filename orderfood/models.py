from django.db import models
from django.core.validators import MinValueValidator
from category.models import Category
from orderfood.choices import StatusChoices
from users.models import TgUser
from users.models import User


# class StatusChoices(models.TextChoices):
#     PREPARING = "preparing", "Preparing"
#     DELIVERING = "delivering", "Delivering"
#     DELIVERED = "delivered", "Delivered"


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='media/media/food_images/')  # Example path, adjust as needed
    category = models.ForeignKey(Category, related_name="category_foods", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Order(models.Model):
    total_price = models.FloatField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    telegram_user = models.ForeignKey(TgUser, related_name="orders_telegram_user", on_delete=models.CASCADE)
    delivered_by = models.ForeignKey(User, related_name="orders_delivered", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    delivered_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        # ordering = [""]

    def __str__(self):
        return self.description


class OrderFood(models.Model):
    order = models.ForeignKey(Order, related_name="order_foods", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="ordered_foods", on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Basket(models.Model):
    user = models.ForeignKey(User, related_name="user_basket", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="food_basket", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.firstname}'ning savatchasi"
