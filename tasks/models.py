from django.conf import settings
from django.db import models

from shots.models import Shot


class TaskStatus(models.Model):
    created_at = models.DateTimeField(
        "когда создан",
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_statuses",
        verbose_name="кем создан",
    )
    title = models.CharField(
        "Статус задачи",
        max_length=50,
    )

    def __str__(self) -> str:
        return f"{self.title}"


class Task(models.Model):
    created_at = models.DateTimeField(
        "когда создана",
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_tasks",
        verbose_name="кем создана",
    )
    description = models.TextField("описание")
    shot = models.ForeignKey(
        Shot,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="относится к шоту",
    )
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="статус",
    )

    def __str__(self) -> str:
        return f"{self.description}"
