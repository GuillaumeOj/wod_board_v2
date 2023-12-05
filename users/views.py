from typing import Any

from django.http import HttpRequest
from drf_spectacular.utils import PolymorphicProxySerializer, extend_schema
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from users.models import User
from users.serializers import UserCreateSerializer, UserDetailSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        parser_context: dict[str, Any] = getattr(self.request, "parser_context")
        if not parser_context:
            return super().get_serializer_class()

        user_detail_id = parser_context["kwargs"].get("pk")
        # If the request user is anonymous, they don't have an id
        request_user_id = getattr(self.request.user, "id")
        request_user_is_staff = getattr(self.request.user, "is_staff")

        if (
            user_detail_id
            and request_user_id
            and (user_detail_id == str(request_user_id) or request_user_is_staff)
        ):
            return UserDetailSerializer

        request_method = self.request.method
        if request_method == "POST" or (
            request_method in ["PUT", "PATCH"]
            and user_detail_id
            and request_user_id
            and (user_detail_id == str(request_user_id) or request_user_is_staff)
        ):
            return UserCreateSerializer

        return super().get_serializer_class()

    @extend_schema(
        responses={
            200: PolymorphicProxySerializer(
                component_name="UserDetailOrNot",
                serializers=[UserSerializer, UserDetailSerializer],
                resource_type_field_name=None,
            )
        }
    )
    def retrieve(self, request: HttpRequest, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(responses=UserCreateSerializer)
    def partial_update(self, request: HttpRequest, *args, **kwargs) -> Response:
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(responses=UserCreateSerializer)
    def update(self, request: HttpRequest, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)
