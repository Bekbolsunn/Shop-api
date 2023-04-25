from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from users.models import ConfirmCode


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        return password


class UserLoginValidateSerializer(UserValidateSerializer):
    pass


class UserCreateValidateSerializer(UserValidateSerializer):
    is_active = serializers.BooleanField(default=False, required=False)
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("User already exists! ")

class ConfirmUserValidateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_user_id(self, user_id):
        try:
            ConfirmCode.objects.get(id=user_id)
        except ConfirmCode.DoesNotExist:
            return user_id
        raise ValidationError("User_id does not exists!")
    