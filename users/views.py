from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import Response

from users.serializers import (
    UserAuthTokenSerializer,
    UserDetailSerializer,
    UserRegisterSerializer,
)


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {
                "user": serializer.data,
                "token": token,
            },
            status=HTTP_201_CREATED,
            headers=headers,
        )


class UserLoginView(LoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super().post(request, format=format)


class UserProfileView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user
