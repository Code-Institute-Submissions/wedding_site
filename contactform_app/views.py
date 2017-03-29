from django.shortcuts import render
from contactform_app.forms import ContactForm


# Create your views here.


def contact(request):
    form_class = ContactForm

    return render(request, 'contactform.html', {
        'form': form_class,
    })