from django.urls import path

from .views import cart, cart_add,add_cart,cart_detail,cart_remove

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path("c", cart, name="cart"),
    path('add/<int:product_id>/',cart_add, name='cart_add'),
    path("add/cart", add_cart, name="add_cart"),
    path('remove/<int:product_id>/', cart_remove,
                            name='cart_remove'),
]
