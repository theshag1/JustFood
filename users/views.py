from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .serializer import ProfileSerializer, UserRegister, LoginSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProfileApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(username=request.user.username)
        serializer_class = ProfileSerializer(queryset)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRegisterApiview(generics.CreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserRegister


class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializers = LoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        username = serializers.validated_data.get('username')
        password = serializers.validated_data.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            authenticate(request, password=password, username=username)
            return Response(serializers.data)
        else:
            return Response({'detail': 'Please enter the correct username and password'})
