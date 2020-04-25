from factory.faker import Faker

from core.factories import BaseModelFactory
from users.models import User


class UserFactory(BaseModelFactory):
    class Meta:
        model = User

    is_staff = False
    is_superuser = False

    email = Faker("safe_email")
