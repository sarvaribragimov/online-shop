from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.accounts"

    # ready method is called when the app is ready to be used
    def ready(self):
        import src.apps.accounts.signals  # noqa
