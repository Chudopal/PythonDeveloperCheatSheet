from .models import Event
from .serializers import EventSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EventListView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
