from unittest.mock import Mock

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from core.models import BaseModel, UserOwnerMixin
from .managers import UserManager
from .utils import picture_path


class User(AbstractBaseUser, PermissionsMixin, BaseModel, UserOwnerMixin):
    email = models.EmailField(
        "email address", unique=True, help_text="email do usuário"
    )

    password = models.CharField("senha", max_length=128, help_text="senha do usuário")

    _picture = models.ImageField(
        "imagem de perfil",
        upload_to=picture_path,
        help_text="imagem de perfil",
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="usuário tem acesso à " "interface admin?",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["email"]
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    @property
    def user_owner(self):
        return self

    @property
    def picture(self):
        try:
            # noinspection PyStatementEffect
            self._picture.url
            return self._picture
        except ValueError:
            return Mock(url="/static/picture/defaultavatar.png")

    @picture.setter
    def picture(self, value):
        self._picture = value
