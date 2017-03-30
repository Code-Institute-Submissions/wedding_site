from django.shortcuts import render
from .models import Event
from django.db.models.base import ObjectDoesNotExist

# Create your views here.


def userevent(request):
    try:
        event = Event.objects.get(owner=request.user)
        return render(request, 'event_details.html', {'event': event})

    except ObjectDoesNotExist:
        return render(request, 'no_event.html')
