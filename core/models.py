import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = models.Manager()

    class Meta:
        abstract = True


class UserOwnerMixin(object):
    @property
    def user_owner(self):
        raise NotImplementedError("Sub model must implement this method!")


class UserParticipantsMixin(object):
    @property
    def user_participants(self):
        raise NotImplementedError("Sub model must implement this method!")
