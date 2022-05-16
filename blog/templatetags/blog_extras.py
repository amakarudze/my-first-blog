from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag(takes_context=True)
def get_context(context):
    recaptcha_site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY

    return {"recaptcha_site_key": recaptcha_site_key}
