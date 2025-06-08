from import_export import resources, fields
from .models import MEvent

class MEventResource(resources.ModelResource):
    username = fields.Field(attribute='user__username', column_name='username')

    class Meta:
        model = MEvent
        fields = (
            'content_type',
            'name',
            'url',
            'admin_url',
            'notes',
            'date_posted',
            'event_class',
            'user',
            'groups',
            'request',
            'bucket',
            'data',
            'scope',
            'username'
        )
