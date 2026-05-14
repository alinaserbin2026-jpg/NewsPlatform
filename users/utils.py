from django.urls import reverse

from .models import Invitation
from django.core.mail import send_mail


def create_invitation(email: str, inviter=None, request=None):

    invitation = Invitation.objects.filter(email=email).delete()

    invite = Invitation.objects.create(email=email)

    url = request.build_absolute_uri(
        reverse("accept-invite", kwargs={"key": str(invite.key)})
    )
    subject = "You're invited to join!"
    message = f"""
    Hello!

    You have been invited to join our website.

    Please click the link below to activate your account and set your password:

    {url}

    This link will be valid for 2 days."""
    send_mail(
        subject,
        message,
        inviter.email,  # from
        [email],  # to
        fail_silently=False,
    )

    return invite