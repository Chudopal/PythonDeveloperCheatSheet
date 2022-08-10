from rest_framework import generics
from plan.models import Event
from .serializers import EventSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
