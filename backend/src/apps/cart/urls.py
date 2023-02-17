from base64 import urlsafe_b64decode
from django.urls import path

from .views import add_cart,cart ,delete_cart, add_to_cart,remove_cart_item

urlpatterns = [
    
    path("", cart, name="cart"),
    path('add/cart', add_cart, name="add_cart"),
    path("delete/<int:cart_item_id>", delete_cart, name="delete_cart"),
    path("remove/<int:cart_item_id>", remove_cart_item, name="remove_cart_item"),
    path('add/<int:cart_item_id>',add_to_cart,name="ad_to_cart"),

   
]
