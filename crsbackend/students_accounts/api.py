from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .serializers import UserSerializer, ComplainantSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = ComplainantSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [BasicAuthentication]
    
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)

        obj = super(LoginAPI, self).post(request, format=None)
        obj.data['user'] = UserSerializer(user).data

        return Response(obj.data)


class ComplainantAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ComplainantSerializer
    
    def get_object(self):
        return self.request.user


class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user