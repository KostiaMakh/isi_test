from django.contrib.auth import get_user_model

from rest_framework import serializers

from threads.serializers import ThreadCreateSerializer

User = get_user_model()

class UserRetrieveSerializer(serializers.ModelSerializer):
    threads = ThreadCreateSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'updated_at',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'threads',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )
