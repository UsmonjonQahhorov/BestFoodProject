from django.db import models


class StatusChoices(models.TextChoices):
    AVAILABLE = ("available", "Available")
    UNAVAILABLE = ("unavailable", "Unavailable")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"
