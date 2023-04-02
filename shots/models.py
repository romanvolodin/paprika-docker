from django.conf import settings
from django.db import models

from projects.models import Project


class ShotGroup(models.Model):
    title = models.CharField(
        "название группы шотов",
        max_length=50,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name="shot_groups",
        verbose_name="про",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_shot_groups",
        verbose_name="кем создан",
    )
    created_at = models.DateTimeField(
        "когда создан",
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f"{self.project.name} {self.title}"


class Shot(models.Model):
    title = models.CharField(
        "Название шота",
        max_length=50,
    )
    group = models.ForeignKey(
        ShotGroup,
        on_delete=models.CASCADE,
        related_name="shots",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_shots",
        verbose_name="кем создан",
    )
    created_at = models.DateTimeField(
        "когда создан",
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.title


class Version(models.Model):
    title = models.CharField(
        "Название версии",
        max_length=50,
    )
    shot = models.ForeignKey(
        Shot,
        on_delete=models.PROTECT,
        related_name="versions",
    )
    video = models.FileField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_versions",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.shot.title} {self.title}"
