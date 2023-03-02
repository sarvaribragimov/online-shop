from django.urls import path

from .views.checkout import checkout
from .views.save_orders import save_orders
from .views.order_list import order_list


urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("order-save/", save_orders, name="save_orders"),
    path('list/',order_list,name="order_list"),
]
