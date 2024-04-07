from django.db import models

from tcms.utils.models_utils import only_int, adhar_digit


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    date_of_birth = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, db_index=True, unique=True)
    adhar_number = models.CharField(null=False, max_length=12, blank=False, validators=[only_int, adhar_digit])
    registration_date = models.DateField(auto_now_add=True)
    mobile_number = models.CharField(null=False, max_length=10, blank=False)

    def __str__(self):
        return self.name
