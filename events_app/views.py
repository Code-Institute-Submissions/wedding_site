from django.shortcuts import render
from .models import Event
from django.db.models.base import ObjectDoesNotExist
import stripe
from stream3_project import settings

# Create your views here.


def userevent(request):
    try:
        event = Event.objects.get(owner=request.user)
        return render(request, 'event_details.html', {'event': event})

    except ObjectDoesNotExist:
        return render(request, 'no_event.html')


def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    token = request.POST['stripeToken']
    email = request.POST['stripeEmail']
    amount = 10000

    customer = stripe.Customer.create(
        email=email,
        card=token
    )

    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='eur',
        description='Deposit Payment'
    )

    return render(request, 'charge.html')
