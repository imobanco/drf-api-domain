from factory import DjangoModelFactory
from factory.faker import Faker

from .models import BaseModel


class BaseModelFactory(DjangoModelFactory):
    id = Faker("uuid4")

    class Meta:
        model = BaseModel
        abstract = True
