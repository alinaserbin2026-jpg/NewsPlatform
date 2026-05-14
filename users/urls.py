from django.urls import path
from .views import accept_invite

urlpatterns = [
    path("invite/<uuid:key>/", accept_invite, name="accept_invite"),
]
