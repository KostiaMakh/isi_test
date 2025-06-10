from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from rest_framework import serializers
from threads.models import (
    Thread,
    Message,
)


User = get_user_model()


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
        )


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'sender',
            'text',
            'thread',
            'created_at',
            'updated_at',
            'is_read',
        )


class MessageRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'sender',
            'text',
            'created_at',
            'updated_at',
            'is_read',
        )


class ThreadSerializer(serializers.ModelSerializer):
    messages = MessageRepresentationSerializer(many=True)
    participants = ParticipantSerializer(many=True)

    class Meta:
        model = Thread
        fields = (
            'id',
            'participants',
            'created_at',
            'updated_at',
            'messages',
        )


class ThreadCreateSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        write_only=True
    )

    class Meta:
        model = Thread
        fields = (
            'participants',
        )

    def validate_participants(self, value):
        if len(set(value)) != 2:
            raise serializers.ValidationError("Exactly two unique participants are required.")
        return value

    def create(self, validated_data):
        participants = validated_data['participants']
        participant_ids = sorted(user.id for user in participants)

        # Check existing of similar thread
        existing_threads = Thread.objects.annotate(num_participants=Count('participants')).filter(num_participants=2)
        for thread in existing_threads:
            thread_participant_ids = sorted(thread.participants.values_list('id', flat=True))
            if thread_participant_ids == participant_ids:
                return thread

        # create new
        thread = Thread.objects.create()
        thread.participants.set(participants)
        return thread

