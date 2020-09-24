import uuid

from django.conf import settings
from django.contrib.auth import password_validation
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    PasswordField,
)
from rest_framework_simplejwt.tokens import RefreshToken

from src.core.utils.send_mail import send_email_celery
from src.apps.account.choices import AccountTypeChoices
from src.apps.account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "avatar",
            "about",
            "vk_profile",
            "fb_profile",
            "inst_profile",
            "tg_profile",
        )


class SignInSerializer(TokenObtainPairSerializer):

    email = serializers.EmailField(validators=[EmailValidator()])
    password = PasswordField(write_only=True)

    class Meta:
        fields = ("email", "password")

    def get_username(self, obj):
        return self.email


class PasswordValidator(object):
    def __call__(self, password):
        password_validation.validate_password(password)


# TODO: go utils
def set_code(email):
    key = str(uuid.uuid4()).replace("-", "")
    settings.REDIS_CONNECT.set(email, key, ex=300)
    return key


def get_code(key):
    return settings.REDIS_CONNECT.get(key)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    password = serializers.CharField(validators=[PasswordValidator()])

    class Meta:
        fields = (
            "email",
            "password",
        )

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"{email} already exists")
        return email

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        username = email.lower().split("@")[0]
        user = User.objects.create_user(
            username=username,
            email=email.lower(),
            password=password,
            account_type=AccountTypeChoices.CLIENT,
        )

        code = set_code(email.lower())
        message = f"{code}"
        send_email_celery.delay(to=[email], subject=_("Welcome"), message=message)
        return user

    def to_representation(self, instance):
        token = RefreshToken.for_user(instance)
        return {"access": str(token.access_token)}


class SignOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    country = CountryField(required=False)
    email = serializers.CharField(validators=[EmailValidator()], required=False)
    avatar = serializers.CharField(source="get_avatar_url")

    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
            "first_name",
            "last_name",
            "birth_date",
            "country",
            "city",
            "address",
            "email",
            "is_email_confirmed",
            "is_profile_full",
            "phone_number",
            "vk_profile",
            "fb_profile",
            "inst_profile",
            "tg_profile",
        )


class ConfirmSerializer(serializers.Serializer):
    email = serializers.CharField(validators=[EmailValidator()], required=False)
    code = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = User

    def validate_code(self, code):
        return code
