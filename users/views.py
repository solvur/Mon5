from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from users.models import Confirm_User
from users.serializers import ConfirmUserSerializer


@api_view(['POST'])
def confirm_user(request):
    serializer = ConfirmUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        if Confirm_User.objects.filter(code=request.data['code']):
            User.objects.update(is_active=True)
            return Response(status=status.HTTP_200_OK,
                            data={'Ok!': 'User is active'})
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Code or id not found!'})
    except ValueError:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'error': 'value error'})