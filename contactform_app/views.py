from django.shortcuts import render, redirect
from contactform_app.forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.template.loader import get_template
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
            "Message: " "%s" \
            "Event Type: " "%s" \
            "Event Package: " "%s" \
            % (
                form_full_name,
                form_email,
                form_message,
                event_type,
                event_package
            )


        # Email the profile with the
            # contact information
            # template = get_template('contact_template.txt')
            # context = Context({
            #     'full_name': full_name,
            #     'email': email,
            #     'event_type': event_type,
            #     'event_package': event_package,
            #     'message': message
            # })
            # content = template.render(context)

            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "Your website" + '',
            #     ['youremail@gmail.com'],
            #     headers={'Reply-To': email}
            # )

        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
            )
            # return redirect('contact')
    context = {
        "form": form,
    }
    return render(request, 'successs.html', context)

