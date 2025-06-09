from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import (
    UserRetrieveSerializer,
    UserCreateSerializer,
)


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer

    @swagger_auto_schema(
        request_body=UserCreateSerializer(),
        responses={
            status.HTTP_201_CREATED: UserRetrieveSerializer()
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        thread = serializer.save()
        output_serializer = UserRetrieveSerializer(thread)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
