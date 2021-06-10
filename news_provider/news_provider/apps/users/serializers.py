from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

# Get the UserModel
UserModel = get_user_model()


class SignUpSerializer(serializers.Serializer):
    """Serializer for sign-up"""
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=40)
    first_name = serializers.CharField(max_length=25, required=False)
    last_name = serializers.CharField(max_length=25, required=False)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    def create(self, validated_data):
        user = UserModel(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate_email(self, email):
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists', })
        return email

    def validate(self, data):
        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)

        if password is not None and password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'Passwords did not match.', })

        return data
