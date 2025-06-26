from datetime import datetime

from django.template import Library
from django.utils import timezone

register = Library()


@register.filter()
def format_empty_data(data):
    if data in (None, "", 0.0, []):
        return "N/A"

    return data


@register.filter()
def field_name_to_label(value):
    if value:
        return value.replace("_", " ").capitalize()
    return None


@register.filter(expects_localtime=True)
def parse_datetime(value):
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M")  # noqa: DTZ007
    except ValueError:
        return None


@register.filter(expects_localtime=True)
def parse_iso_datetime(value):
    try:
        return timezone.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return None
