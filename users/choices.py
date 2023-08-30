from django.db import models


class RoleChoices(models.TextChoices):
    OPERATOR = ("operator", "Operator")
    ADMIN = ("admin", "Admin")
    DELIVER = ("deliver", "Deliver")
