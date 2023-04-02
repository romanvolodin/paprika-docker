from import_export import resources

from .models import Shot, ShotGroup


class ShotGroupResource(resources.ModelResource):
    class Meta:
        model = ShotGroup
        skip_unchanged = True

    def before_import_row(self, row, **kwargs):
        row["created_by"] = kwargs["user"].id


class ShotResource(resources.ModelResource):
    class Meta:
        model = Shot
        skip_unchanged = True

    def before_import_row(self, row, **kwargs):
        row["created_by"] = kwargs["user"].id
