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
    path(
        "",
        include(
            (
                "src.apps.store.urls",
                "src.apps.store.urls",
            ),
            namespace="store",
        ),
    ),
]
