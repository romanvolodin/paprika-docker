# Generated by Django 4.1.1 on 2023-04-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NOT_STARTED", "Не начата"),
                            ("IN_PROGRESS", "В процессе"),
                            ("DONE", "Выполнена"),
                            ("COMMENTED", "Есть комментарии"),
                            ("APPROVED", "Принята"),
                        ],
                        max_length=11,
                        verbose_name="Статус задачи",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statuses",
                        to="tasks.task",
                        verbose_name="относится к задаче",
                    ),
                ),
            ],
        ),
    ]