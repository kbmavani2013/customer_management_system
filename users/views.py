from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import UserSerializer


@api_view(['POST'])
def user_register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': "User created successfully", 'data': serializer.data,
                         'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': serializer.error_messages, 'data': [], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
