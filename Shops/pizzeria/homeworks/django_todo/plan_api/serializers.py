from rest_framework import serializers
from plan.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'created_at', 'started_at', 'finished_at', 'title', 'description', 'depends_on', 'status']
