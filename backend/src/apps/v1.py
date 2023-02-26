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
        "store/",
        include(
            (
                "src.apps.store.urls",
                "src.apps.store.urls",
            ),
            namespace="store",
        ),
    ),
    path(
        "cart/",
        include(
            (
                "src.apps.cart.urls",
                "src.apps.cart.urls",
            ),
            namespace="cart",
        ),
    ),
    path(
        "order/",
        include(
            (
                "src.apps.order.urls",
                "src.apps.order.urls",
            ),
            namespace="order",
        ),
    ),
    
]
