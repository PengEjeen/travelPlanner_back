from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer , UsernameRetrievalSerializer , UserSerializer ,PasswordRetrievalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data


        token = validated_data['token']
        user = validated_data['user']

        return Response({
            "token": token.key,
            "username": user.username
        }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user_by_username(request):
    # 'username'을 요청 데이터에서 받아오기
    username = request.data.get('username')

    if not username:
        return Response({"error": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response({"message": "User account deleted successfully."}, status=status.HTTP_200_OK)



@api_view(['GET'])  #유저 정보 가져오기
def get_user_info(request, username):
    try:

        user = User.objects.get(username=username)
    except User.DoesNotExist:

        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)


    return Response(serializer.data, status=status.HTTP_200_OK)


class UsernameRetrievalView(APIView):  # ID 찾기
    def post(self, request):
        serializer = UsernameRetrievalSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.get_username()
            return Response({"username": username}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordRetrievalView(APIView): ##비번찾기
    def post(self, request):
        serializer = PasswordRetrievalSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.get_password()
            return Response({"password": password}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

