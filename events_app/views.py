from django.shortcuts import render, get_object_or_404
from .models import Event
# Create your views here.

def event(request, id):
    event = get_object_or_404(Event, pk=id)

    if request.user == event.owner:
        return render(request, 'event_details.html', {'event': event})
    else:
