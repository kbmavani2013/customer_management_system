from django.urls import path

from plans.views import create_plan, update_plan, get_plan

urlpatterns = [
    path('', get_plan),
    path('create/', create_plan),
    path('change/', update_plan)
]