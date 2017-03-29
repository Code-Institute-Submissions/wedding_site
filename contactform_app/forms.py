from django import forms

EVENT_TYPE_CHOICES = (
    ('civil ceremony', 'Civil Ceremony'),
    ('church ceremony', 'Church Ceremony'),
    ('drinks deception', 'Drinks Reception'),
    ('dinner music', 'Dinner Music'),
    ('other', 'Other'),
)

EVENT_PACKAGE_CHOICES = (
    ('voice & piano', 'Voice & Piano'),
    ('voice & harp', 'Voice & Harp'),
    ('piano instrumental', 'Piano instrumental'),
    ('harp instrumental', 'Harp instrumental'),
    ('other/undecided', 'Other/Undecided'),
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

    event_package = forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=EVENT_PACKAGE_CHOICES,
    )


    cc_myself = forms.BooleanField(required=False)
