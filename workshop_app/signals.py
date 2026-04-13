from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def ensure_profile_for_user(sender, instance, created, **kwargs):
    """Ensure every non-superuser has a profile row."""
    if instance.is_superuser:
        return

    Profile.objects.get_or_create(
        user=instance,
        defaults={
            "institute": "Unknown Institute",
            "department": "computer engineering",
            "phone_number": "0000000000",
            "position": "coordinator",
            "is_email_verified": True,
        },
    )
