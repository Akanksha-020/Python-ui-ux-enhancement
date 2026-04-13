from __future__ import unicode_literals

from django.apps import AppConfig


class WorkshopAppConfig(AppConfig):
    name = 'workshop_app'

    def ready(self):
        # Import signal handlers when app registry is ready.
        from . import signals  # noqa: F401
