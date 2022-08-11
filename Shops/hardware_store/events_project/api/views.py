from .models import Event
from .serializer import EventSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class EventListView(ListCreateAPIView):
    queryset = Event.object.all()
    serializer_class = EventSerializer

class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Event.object.all()
    serializer_class = EventSerializer

