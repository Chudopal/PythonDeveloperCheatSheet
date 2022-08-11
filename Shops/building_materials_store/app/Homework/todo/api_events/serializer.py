from rest_framework.serializers import ModelSerializer
from plan.models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "created_at", "started_at", "finished_at", "title", "description", "depends_on", "status"]


