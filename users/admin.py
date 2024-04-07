from django.contrib import admin

from users.models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number', 'registration_date')
    search_fields = ('name', 'email', 'mobile_number')


admin.site.register(User, UsersAdmin)
