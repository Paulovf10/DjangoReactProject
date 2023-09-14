from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'custom_auth'
    verbose_name = '1. USUÁRIOS'


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = '2. CORE'
