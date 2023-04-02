from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportMixin

from .models import Shot, ShotGroup, Version
from .resources import ShotGroupResource, ShotResource


@admin.register(ShotGroup)
class ShotGroupAdmin(ImportMixin, admin.ModelAdmin):
    resource_classes = (ShotGroupResource,)


class VersionInline(admin.TabularInline):
    model = Version
    show_change_link = True
    extra = 0


@admin.register(Shot)
class ShotAdmin(ImportMixin, admin.ModelAdmin):
    list_display = (
        "title",
        "group",
        "created_by",
        "created_at",
        "get_latest_version",
    )
    list_filter = (
        "group__project",
        "group",
    )
    inlines = (VersionInline,)
    resource_classes = (ShotResource,)

    @admin.display(description="Latest version")
    def get_latest_version(self, obj):
        latest_version = obj.versions.latest("created_at")
        if latest_version:
            return mark_safe(
                f'<a href="{latest_version.video.url}">{latest_version.title}</a>'
            )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    pass
