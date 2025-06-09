from django.contrib import admin

from threads.models import (
    Thread,
    Message,
)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_participants',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'participants__email',
        'participants__first_name',
        'participants__last_name'
    )
    ordering = ('-created_at',)

    def display_participants(self, obj):
        return ", ".join([f"{user.get_full_name()} ({user.email})" for user in obj.participants.all()])

    display_participants.short_description = 'Participants'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'thread',
        'short_message',
        'sender',
        'is_read',
        'created_at'
    )
    search_fields = (
        'text',
        'sender__email',
        'thread__id'
    )
    list_filter = (
        'is_read',
    )
    ordering = (
        '-created_at',
    )

    def short_message(self, obj):
        return obj.text[:30] + ('...' if len(obj.text) > 30 else '')

    short_message.short_description = 'Message'
