from rest_framework import serializers

from ..models import User

__all__ = (
    'UserSerializer',
    'UserCreationSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'nickname',
            'password',
            'img_profile',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'ori_password',
            'password1',
            'password2',
            'img_profile',
        )
        read_only_fields = (
            'username',
        )


class UserCreationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=30)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('username already exist')
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords didn't match")
        return data

    def save(self, *args, **kwargs):
        username = self.validated_data.get('username', '')
        nickname = self.validated_data.get('nickname', '')
        password = self.validated_data.get('password1', '')
        user = User.objects.create_user(
            username=username,
            nickname=nickname,
            password=password
        )
        return user
