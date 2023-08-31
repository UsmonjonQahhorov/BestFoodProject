from django.db import models

from users.choices import RoleChoices


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
    chat_id = models.CharField(max_length=50, default=0)
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    is_blocked = models.BooleanField(default=False)
    is_veryfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "TgUser"
        verbose_name_plural = "TgUsers"
        ordering = ["fullname"]

    def __str__(self):
        return f"{self.fullname}"


class Sms(models.Model):
    sms = models.CharField(max_length=6)
    telegram_user = models.ForeignKey(TgUser, related_name="tu_sms", on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
