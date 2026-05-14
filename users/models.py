# import string
# import uuid
# from django.utils import timezone
# from datetime import timedelta
# from random import random
#
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin
# from django.db import models
#
#
# class Invitation(models.Model):
#     email = models.EmailField(max_length=255, unique=True)
#     key = models.UUIDField(default=uuid.uuid4, editable=False)
#     created = models.DateTimeField(auto_now_add=True)
#     expired = models.DateTimeField(blank=True, null=True)
#
#     is_used = models.BooleanField(default=False)
#
#
#     def save(self, *args, **kwargs):
#         if  not self.expired:
#             self.expired =  timezone.now() + timedelta(days=2)  # срок жизни
#         super().save(*args, **kwargs)
#
# #
# # def generate_random_password(length=12):
# #     characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
# #     password = ''.join(random.choice(characters) for _ in range(length))
# #     return password
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#
#         if password is None:
#             password = generate_random_password()
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('role', 1)  # ADMIN
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     class Role(models.IntegerChoices):
#         ADMIN = 1, 'Admin'
#         MODERATOR = 2, 'Moderator'
#         CONTENT_MANAGER = 3, 'Content Manager'
#
#     class InviteStatus(models.IntegerChoices):
#         PENDING = 1, 'Pending'
#         ACCEPTED = 2, 'Accepted'
#
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True, blank=True, null=True)
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
#
#     role = models.IntegerField(choices=Role.choices, default=Role.CONTENT_MANAGER)
#     invite_status = models.IntegerField(choices=InviteStatus.choices, default=InviteStatus.PENDING)
#
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email