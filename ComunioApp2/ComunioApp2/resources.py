from import_export import resources
from players.models import Players


class PlayerResource(resources.ModelResource):
    class Meta:
        model = Players
