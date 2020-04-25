from core.services import ModelService
from .models import User


class UserService(ModelService):
    MODEL = User

    @classmethod
    def create(cls, password=None, **kwargs):
        user = User(**kwargs)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def list_for_request(cls, request):
        user = request.user
        if user.is_superuser:
            return cls.list()
        else:
            return cls.filter(id=user.id)
