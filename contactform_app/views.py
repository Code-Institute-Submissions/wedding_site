from django.shortcuts import render, render_to_response
from contactform_app.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            form_full_name = form.cleaned_data.get("full_name")
            subject = 'Wedding site contact form'
            event_type = form.cleaned_data.get("event_type")
            event_package = form.cleaned_data.get("event_package")
            phone_number = form.cleaned_data.get("phone_number")
            event_date = form.cleaned_data.get("event_date")
            from_email = settings.EMAIL_HOST_USER
            to_email = ['bren.c.long@gmail.com']
            cc_myself = form.cleaned_data['cc_myself']
            if cc_myself:
                to_email.append('form_email')

            contact_message = \
                "Name: " "%s" "\n" \
                "\n" \
                "Email: " "%s" "\n" \
                "\n" \
                "Phone Number: " "%s" "\n" \
                "\n" \
                "Event Type: " "%s" "\n" \
                "\n" \
                "Event Package: " "%s" "\n" \
                "\n" \
                "Date: " "%s" "\n" \
                "\n" \
                "Message:" "\n" \
                "%s" \
                % (
                    form_full_name,
                    form_email,
                    phone_number,
                    event_type,
                    event_package,
                    event_date,
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

        return render(request, 'contactsuccess.html', context)
    return render(request, 'contactform.html', {'form': form})
