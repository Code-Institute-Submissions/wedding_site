from django import forms

EVENT_TYPE_CHOICES = (
    ('Civil Ceremony', 'Civil Ceremony'),
    ('Church Ceremony', 'Church Ceremony'),
    ('Drinks Reception', 'Drinks Reception'),
    ('Dinner Music', 'Dinner Music'),
    ('Other', 'Other'),
)

EVENT_PACKAGE_CHOICES = (
    ('Voice & Piano', 'Voice & Piano'),
    ('Voice & Harp', 'Voice & Harp'),
    ('Piano instrumental', 'Piano instrumental'),
    ('Harp instrumental', 'Harp instrumental'),
    ('Other/Undecided', 'Other/Undecided'),
)


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50)

    last_name = forms.CharField(required=True, max_length=50)

    email_address = forms.EmailField(required=True, max_length=50)

    event_location = forms.CharField(required=True, max_length=50)

    event_type = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=EVENT_TYPE_CHOICES,
    )

    event_package = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=EVENT_PACKAGE_CHOICES,
    )

    your_message = forms.CharField(
        required=True,
        max_length=1000,
        widget=forms.Textarea,
    )

    cc_myself = forms.BooleanField(required=False)
