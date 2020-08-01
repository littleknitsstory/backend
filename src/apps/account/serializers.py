import uuid

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

from src.settings.components.cache import redis_connect as rc
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

    username = serializers.SerializerMethodField()
    email = serializers.EmailField(validators=[EmailValidator()])
    password = PasswordField(write_only=True)

    class Meta:
        fields = ("email", "password")

    def get_username(self, obj):
        return self.email

    def create(self, validated_data):
        return validated_data

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data.pop("refresh")
        data["access"] = str(refresh.access_token)
        return data


class PasswordValidator(object):
    def __call__(self, password):
        password_validation.validate_password(password)


def set_code(email):
    key = str(uuid.uuid4()).replace("-", "")
    rc.set(email, key, ex=300)

    is_code = get_code(key)
    print(rc.get(email))
    print(is_code)


def get_code(key):
    return rc.get(key)


class SignUpSerializer(serializers.Serializer):
    # username
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

    # TODO: чето решить с username=email.lower()
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=str(email.lower()),
            email=email.lower(),
            password=password,
            account_type=AccountTypeChoices.CLIENT,
        )
        print(type(email.lower()))
        code = f"{1234}"
        code = set_code(email.lower())
        send_email_celery.delay(to=[email], subject=_("Welcome"), message=f"{code}")
        # user.save()

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
