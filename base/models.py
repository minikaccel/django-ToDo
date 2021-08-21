from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Not required")
    description = models.TextField(blank=True, null=True, help_text="Not required")
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        order_with_respect_to = 'user'