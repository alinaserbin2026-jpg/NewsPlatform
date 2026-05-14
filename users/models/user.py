
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .usermanager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        MODERATOR = 2, 'Moderator'
        CONTENT_MANAGER = 3, 'Content Manager'

    class InviteStatus(models.IntegerChoices):
        PENDING = 1, 'Pending'
        ACCEPTED = 2, 'Accepted'

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    role = models.IntegerField(choices=Role.choices, default=Role.CONTENT_MANAGER)
    invite_status = models.IntegerField(choices=InviteStatus.choices, default=InviteStatus.PENDING)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email