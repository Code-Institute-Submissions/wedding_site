from django.shortcuts import render
from contactform_app.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


# def contact(request):
#     form_class = ContactForm
#
#     return render(request, 'contactform.html', {
#         'form': form_class,
#     })


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Wedding site contact form'
        event_type = form.cleaned_data.get("event_type")
        event_package = form.cleaned_data.get("event_package")
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]

        contact_message = \
            "Name: " "%s" \
            "Email: " "%s" \
            "Event Type: " "%s" \
            "Event Package: " "%s" \
            "Message: " "%s" \
            % (
                form_full_name,
                form_email,
                event_type,
                event_package,
                form_message,
            )

        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
            )
    context = {
        "form": form,
    }

    return render(request, 'successs.html', context)

