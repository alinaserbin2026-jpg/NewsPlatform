import uuid
from django.utils import timezone
from datetime import timedelta
from django.db import models


class Invitation(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    expired = models.DateTimeField(blank=True, null=True)

    is_used = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if  not self.expired:
            self.expired =  timezone.now() + timedelta(days=2)  # срок жизни
        super().save(*args, **kwargs)