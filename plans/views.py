from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from plans.models import Plan
from plans.serializers import PlanSerializer, UserActivePlanSerializer


@api_view(['GET'])
def get_plan(request):
    plans = Plan.objects.filter(plan_status='Active')
    if plans:
        data = PlanSerializer(plans, many=True)
        return Response({'message': "Plan found", 'data': data.data, 'status': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)
    else:
        return Response({'message': "No plan found", 'data': [], 'status': status.HTTP_404_NOT_FOUND},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_plan(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': "Plan created successfully", 'data': serializer.data,
                         'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': serializer.error_messages, 'data': [], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_plan(request):
    serializer = UserActivePlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': "Plan update successfully", 'data': serializer.data,
                         'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': serializer.error_messages, 'data': [], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
