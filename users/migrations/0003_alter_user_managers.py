# Generated by Django 4.1.1 on 2023-12-26 20:29

from django.db import migrations
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.managers.UserManager()),
            ],
        ),
    ]
