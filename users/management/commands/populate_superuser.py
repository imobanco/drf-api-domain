from django.core.management import BaseCommand

from django.contrib.auth import get_user_model

from users.factories import UserFactory


class Command(BaseCommand):
    help = "Create super user"

    def handle(self, *args, **options):
        model = get_user_model()
        if not model.objects.filter(email="superuser@admin.com"):
            superuser = UserFactory(
                email="superuser@admin.com", is_staff=True, is_superuser=True
            )
            superuser.set_password("@Admin123")
            superuser.save()
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.ERROR("Superuser already created!"))
