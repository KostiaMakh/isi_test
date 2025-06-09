from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'email',
        'is_active',
        'is_staff',
        'created_at'
    )
    search_fields = (
        'id',
        'email',
        'first_name',
        'last_name'
    )
    list_filter = (
        'is_active',
        'is_staff',
    )
