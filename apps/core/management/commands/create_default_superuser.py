from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from isi_test.settings.base import DEFAULT_SUPERUSER_EMAIL


class Command(BaseCommand):
    help = 'Create base superuser!'

    def handle(self, *args, **options) -> None:
        user_model = get_user_model()

        user_email = settings.DEFAULT_SUPERUSER_EMAIL
        user_password = settings.DEFAULT_SUPERUSER_PASSWORD

        if not user_email or not user_password:
            self.stdout.write(
                self.style.ERROR('Please set DEFAULT_SUPERUSER_EMAIL and DEFAULT_SUPERUSER_PASSWORD in settings!')
            )
            return

        if not user_model.objects.filter(email=settings.DEFAULT_SUPERUSER_EMAIL).exists():
            user_model.objects.create_superuser(
                email=user_email,
                password=user_password,
            )

        self.stdout.write(
            self.style.ERROR(f'Default superadmin {DEFAULT_SUPERUSER_EMAIL} created')
        )
