from .models import Cart, CartItem,StatusChoices
from ..common.get_cart_id import _cart_id


def counter(request):
    try:
        if request.path.startswith("/admin"):
            return {}
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.get(cart_id_pk=_cart_id(request))
        counter = CartItem.objects.filter(cart=cart,status=StatusChoices.ACTIVE).count()
        return {"counter": counter}
    except Cart.DoesNotExist:
        return {"counter": 0}
