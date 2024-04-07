from django.contrib import admin

from plans.models import Plan, UserActivePlan


class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_cost', 'validity', 'plan_status')
    search_fields = ('plan_name',)
    list_filter = ('plan_status',)


admin.site.register(Plan, PlanAdmin)


class UserActivePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'plan_validity', 'plan_status')


admin.site.register(UserActivePlan, UserActivePlanAdmin)
