# # users/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from django.utils import timezone
# from datetime import timedelta
#
# from .models import User, Invitation
#
#
# @receiver(post_save, sender=User)
# def send_invitation_email(sender, instance, created, **kwargs):
#     if not created or instance.is_active:
#         return  # doar la creare + dacă nu e deja activ
#
#     invitation = Invitation.objects.create(
#         email=instance.email,
#         # expired se setează automat în model
#     )
#
#     # Link-ul (schimbă în producție!)
#     invite_url = f"{settings.SITE_URL}/invite/{invitation.key}/"   # vezi mai jos
#
#     try:
#         send_mail(
#             subject="Invitation to News Project Admin Panel",
#             message=f"Click the link to set your password and activate account:\n\n{invite_url}",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[instance.email],
#             fail_silently=False,
#         )
#         print(f"Invitation email sent to {instance.email}")
#     except Exception as e:
#         print(f"Email failed for {instance.email}: {e}")
from invitations.signals import invite_accepted
from django.dispatch import receiver
