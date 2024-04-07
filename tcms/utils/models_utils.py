from django.core.exceptions import ValidationError


def only_int(value):
    if value.isdigit() is False:
        raise ValidationError('Value must be digit')


def adhar_digit(value):
    if len(value) != 12:
        raise ValidationError('Adhar must be 12 digit')
