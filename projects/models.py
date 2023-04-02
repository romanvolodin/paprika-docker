from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField("название", max_length=150)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="projects",
        verbose_name="кем создан",
    )
    created_at = models.DateTimeField("когда создан", auto_now_add=True)

    def __str__(self):
        return self.name
