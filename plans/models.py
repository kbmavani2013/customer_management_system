from datetime import timedelta, date
from django.db import models

from users.models import User

PLAN_STATUS = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


class Plan(models.Model):
    plan_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    plan_cost = models.PositiveIntegerField(null=False, blank=False)
    validity = models.PositiveIntegerField(null=False, blank=False)
    plan_status = models.CharField(choices=PLAN_STATUS, default='Active', max_length=10)

    def __str__(self):
        return self.plan_name


class UserActivePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    plan_validity = models.DateField(null=True, blank=True)
    plan_status = models.CharField(choices=PLAN_STATUS, default='Active', max_length=10)

    def __str__(self):
        return self.plan_validity.strftime("%Y-%m-%d")

    def save(self, *args, **kwargs):
        if self.plan_status == 'Active':
            self._deactivate_existing_plans()
        if self.plan and self.plan.validity:
            self.plan_validity = self._calculate_plan_validity(self.plan.validity)
        super().save(*args, **kwargs)

    def _calculate_plan_validity(self, validity):
        current_date = date.today()
        plan_validity = current_date + timedelta(days=validity)
        return plan_validity

    def _deactivate_existing_plans(self):
        active_plans = UserActivePlan.objects.filter(user=self.user, plan_status='Active')
        for active_plan in active_plans:
            active_plan.plan_status = 'Inactive'
            active_plan.save()

