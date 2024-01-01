from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user= User.objects.create(
            email='empty_emailll@rambler.ru',
            first_name='Test',
            last_name='Testov',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('Password_empty_emaill1')
        user.save()