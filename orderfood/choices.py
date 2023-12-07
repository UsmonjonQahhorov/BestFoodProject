from django.db import models


class StatusChoices(models.TextChoices):
    PREPARING = "preparing", "Preparing"
    DELIVERING = "delivering", "Delivering"
    DELIVERED = "delivered", "Delivered"