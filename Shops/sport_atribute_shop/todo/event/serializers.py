from rest_framework.serializers import ModelSerializer
from plan.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ["created_at", "started_at", "finished_at", "title", "description", "status"]