from django.contrib.auth import password_validation
from django.core.validators import EmailValidator
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken

from src.apps.account.choices import AccountTypeChoices
from src.apps.account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'avatar',
            'about',
            'vk_profile',
            'fb_profile',
            'inst_profile',
            'tg_profile',
        )


class SignInSerializer(TokenObtainPairSerializer):
    
    username = serializers.SerializerMethodField()
    email = serializers.EmailField(validators=[EmailValidator()])
    password = PasswordField(write_only=True)

    class Meta:
        fields = ('email', 'password')
        
    def get_username(self, obj):
        return self.email

    def create(self, validated_data):
        return validated_data
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data.pop('refresh')
        data['access'] = str(refresh.access_token)
        return data


class PasswordValidator(object):
    def __call__(self, password):
        password_validation.validate_password(password)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    password = serializers.CharField(validators=[PasswordValidator()])

    class Meta:
        fields = ('email', 'password',)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(
            username=email.lower(),
            email=email.lower(),
            password=password,
            account_type=AccountTypeChoices.CLIENT
        )
        user.save()

        return user

    def to_representation(self, instance):
        token = RefreshToken.for_user(instance)
        return {'access': str(token.access_token)}
    
    
class SignOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    country = CountryField(required=False)
    email = serializers.CharField(validators=[EmailValidator()], required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'avatar',
            'first_name',
            'last_name',
            'birth_date',
            'country',
            'city',
            'address',
            'email',
            'is_email_confirmed',
            'is_profile_full',
            'phone_number',
            'vk_profile',
            'fb_profile',
            'inst_profile',
            'tg_profile',
        )
