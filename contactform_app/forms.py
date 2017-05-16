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
    full_name = forms.CharField(required=True, max_length=100)

    email = forms.EmailField(
        required=True,
        max_length=100
    )

    phone_number = forms.IntegerField(
        widget=forms.NumberInput,
    )

    event_location = forms.CharField(
        required=True,
        max_length=100
    )

    event_date = forms.DateField(
        required=True
    )

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

    message = forms.CharField(
        required=True,
        max_length=5000,
        widget=forms.Textarea,
    )

    # cc_myself = forms.BooleanField(required=False)
