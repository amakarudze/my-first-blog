from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import lxml.html


def validate_email_message(message):
    if lxml.html.fromstring(message).find(".//*") is not None:
        raise ValidationError(_("Please enter a valid message."))
