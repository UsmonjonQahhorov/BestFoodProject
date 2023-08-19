from django.db import models


class RoleChoices(models.TextChoices):
    OPERATOR = ("operator", "Operator")
    ADMIN = ("admin", "Admin")
    DELIVER = ("deliver", "Deliver")


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=RoleChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["firstname", "lastname"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class TgUser(models.Model):
    phone_number = models.CharField(max_length=40)
    fullname = models.CharField(max_length=100)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "TgUser"
        verbose_name_plural = "TgUsers"
        ordering = ["fullname"]

    def __str__(self):
        return f"{self.fullname}"
