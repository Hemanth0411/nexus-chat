import email
from django.contrib.auth import get_user_model, authenticate
from django.db.models.sql.query import RawSQL
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _, trim_whitespace

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=5,
        style={'input_type': 'password'}
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password') # password must be in fields to be accepted

    def create(self, validated_data):
        """Create and return a user with an encrypted password."""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs