from __future__ import unicode_literals

from django.apps import AppConfig


class TweeterConfig(AppConfig):
    name = 'tweeter'

    def ready(self):
        import tweeter.signals