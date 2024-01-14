from django.contrib.auth.models import AbstractUser
from django.db import models

from core import consts


class User(AbstractUser):
    role = models.CharField('Роль', max_length=255, choices=consts.ROLE_CHOICES)
