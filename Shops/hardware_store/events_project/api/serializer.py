from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['created_at', 'started_at', 'finished_at', 'title', 'description', 'depends_on', 'status']
