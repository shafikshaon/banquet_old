from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeLog, Status


class User(AbstractUser, TimeLog, Status):
    email = models.EmailField(unique=True, blank=False, null=False)
    member_from = models.DateField(blank=True, null=True)
