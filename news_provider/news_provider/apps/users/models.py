import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Custom user with UUID """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.username
