from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return data


    def create(self, validated_data):
        validated_data.pop('password2')


        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()


        token = Token.objects.create(user=user)
        return user





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return {
                'token': token,
                'user': user
            }
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})

class UserSerializer(serializers.ModelSerializer): #회원정보 보내기
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')


class UsernameRetrievalSerializer(serializers.Serializer):  # ID(username) 찾기
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email.")
        return value

    def get_username(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        return user.username



class PasswordRetrievalSerializer(serializers.Serializer): ##비번찾기
    username = serializers.CharField(required=True)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("No user is associated with this username.")
        return value

    def get_password(self):
        username = self.validated_data['username']
        user = User.objects.get(username=username)
        return user.password