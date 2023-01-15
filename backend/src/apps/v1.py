from django.urls import include, path

urlpatterns = [
    path(
        "",
        include(
            (
                "src.apps.accounts.urls",
                "src.apps.accounts.urls",
            ),
            namespace="accounts",
        ),
    ),
]
