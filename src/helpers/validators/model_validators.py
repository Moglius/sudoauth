import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def _is_valid_path(value):
    pattern = re.compile(r"^/|(/[\w-]+)+$")
    return re.fullmatch(pattern, value)

def _is_valid_hostname(value):
    if len(value) > 253 or len(value) < 4:
        return False
    if value[-1] == ".":
        return False

    labels = value.split(".")

    # the TLD must be not all-numeric
    if re.match(r"[0-9]+$", labels[-1]):
        return False

    allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(label) for label in labels)

def validate_path(value):
    if len(value) < 4 or not _is_valid_path(value):
        raise ValidationError(
            _('%(value)s is not a valid linux path'),
            params={'value': value},
        )

def validate_hostname(value):
    if not _is_valid_hostname(value):
        raise ValidationError(
            _('%(value)s is not a valid hostname'),
            params={'value': value},
        )
