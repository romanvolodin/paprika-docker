from django.contrib import admin

from tasks.models import Task, TaskStatus


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "shot",
        "description",
        "status",
        "created_at",
        "created_by",
    )
    list_filter = (
        "status",
        "created_by",
        "created_at",
    )


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "created_by",
    )
