from django.contrib.auth import get_user_model
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from threads.models import (
    Thread,
    Message,
)
from threads.serializers import (
    ThreadSerializer,
    MessageSerializer,
    MessageCreateSerializer,
    ThreadCreateSerializer,
)


User = get_user_model()


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user = self.request.user
        threads = Thread.objects.filter(participants=user)

        return threads

    @swagger_auto_schema(
        request_body=ThreadCreateSerializer,
        responses={
            status.HTTP_201_CREATED: ThreadSerializer()
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = ThreadCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        thread = serializer.save()
        output_serializer = ThreadSerializer(thread)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=MessageCreateSerializer(),
        responses={
            status.HTTP_201_CREATED: MessageSerializer()
        }
    )
    @action(detail=True, methods=['post'], url_path='send-message')
    def send_message(self, request, pk):
        thread = self.get_object()
        user = self.request.user

        serializer = MessageCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save(
            thread=thread,
            sender=user
        )

        response_serializer = MessageSerializer(message)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        messages = Message.objects.filter(thread__participants=user)

        return messages

    @action(detail=True, methods=['post'], url_path='mark-as-read')
    def mark_as_read(self, request, pk=None):
        try:
            message = self.get_object()
            message.is_read = True
            message.save()
            return Response(
                {"status": "marked as read"},
                status=status.HTTP_200_OK
            )
        except Message.DoesNotExist:
            return Response(
                {"error": "Message not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['get'], url_path='unread-count')
    def unread_count(self, request):
        user = self.request.user
        qs = self.get_queryset()
        count = qs.filter(is_read=False).exclude(sender=user).count()

        return Response({"unread_messages": count})
