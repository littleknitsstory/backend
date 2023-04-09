from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.core.validators import EmailValidator
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    PasswordField,
)
from rest_framework_simplejwt.tokens import RefreshToken

from src.apps.account.choices import AccountTypeChoices

User = get_user_model()


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
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            user = User.objects.create_user(
                username=username,
                email=email.lower(),
                password=password,
                account_type=AccountTypeChoices.CLIENT,
            )
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
            raise serializers.ValidationError("Bad refresh token")


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    country = CountryField(required=False)
    email = serializers.CharField(validators=[EmailValidator()], required=False)
    avatar = serializers.CharField(source="get_avatar_url", required=False)

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
