from django.shortcuts import render, redirect
from contactform_app.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

# Create your views here.


# def contact(request):
#     form_class = ContactForm
#
#     return render(request, 'contactform.html', {
#         'form': form_class,
#     })


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            first_name = request.POST.get(
                'first_name'
            , '')
            last_name = request.POST.get(
                'last_name'
                , '')
            email_address = request.POST.get(
                'email_address'
            , '')
            event_type = request.POST.get(
                'event_type'
                , '')
            event_package = request.POST.get(
                'event_package'
                , '')
            your_message = request.POST.get(
                'your_message'
                , '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'first_name': first_name,
                'last_name': last_name,
                'email_address': email_address,
                'event_type': event_type,
                'event_package': event_package,
                'your_message': your_message
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers={'Reply-To': email_address }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contactform.html', {
        'form': form_class,
    })

