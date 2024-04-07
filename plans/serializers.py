from rest_framework import serializers

from plans.models import Plan, UserActivePlan


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class UserActivePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserActivePlan
        fields = ['user', 'plan']