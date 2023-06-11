from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import Confirm_User


class ConfirmUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_user_id(self, user_id):
        try:
            Confirm_User.objects.get(id=user_id)
        except Confirm_User.DoesNotExist:
            return user_id
        raise ValidationError("User_id does not exists!")
