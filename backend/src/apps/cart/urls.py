from django.urls import path

from .views import cart, cart_add,add_cart

urlpatterns = [
    path("", cart, name="cart"),
    path('add/<int:product_id>/',cart_add, name='cart_add'),
    path("add/cart", add_cart, name="add_cart"),
]
