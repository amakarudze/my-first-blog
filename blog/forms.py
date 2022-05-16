from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Contact
from .validators import validate_email_message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "phone",
            "email",
            "subject",
            "message",
        )

    name = forms.CharField(
        max_length=100,
        label=_("Full Name"),
        widget=(
            forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "FullName",
                    "placeholder": "Full Name",
                }
            )
        ),
    )
    phone = forms.CharField(
        max_length=100,
        label=_("Phone Number"),
        widget=(
            forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "PhoneNumber",
                    "placeholder": "Phone Number",
                }
            )
        ),
    )
    email = forms.CharField(
        max_length=100,
        label=_("Email Address"),
        widget=(
            forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "EmailAddress",
                    "placeholder": "Email Address",
                }
            )
        ),
    )
    subject = forms.CharField(
        max_length=100,
        label=_("Subject"),
        widget=(
            forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Subject",
                    "placeholder": "Subject",
                }
            )
        ),
    )
    message = forms.CharField(
        max_length=100,
        label=_("Message"),
        widget=(
            forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "Message",
                    "rows": "8",
                    "placeholder": "Message",
                }
            )
        ),
    )

    def clean_message(self):
        message = self.cleaned_data.get("message")
        validate_email_message(message)
        return message
