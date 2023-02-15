from base64 import urlsafe_b64decode
from django.urls import path

from .views import cart_add,add_cart,cart_detail,cart_remove

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
   
    path('add/<int:product_id>/',cart_add, name='cart_add'),
    path("add/cart", add_cart, name="add_cart"),
    path("cart/remove/<int:product_id>/", cart_remove,name='cart_remove'),
    # path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]
