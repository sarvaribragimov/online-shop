from django.urls import path

from .views.checkout import checkout
from .views.save_orders import save_orders
urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("order-save/", save_orders, name="save_orders"),
]
