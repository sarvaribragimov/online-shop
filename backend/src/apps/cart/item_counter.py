from .models import CartItem,Cartmodel
from ..common.get_cart_id import _card_id


def counter(request):
    try:
        if request.path.startswith("/admin"):
            return {}
        if request.user.is_authenticated:
            cart = Cartmodel.objects.get(user=request.user)
        else:
            cart = Cartmodel.objects.get(cart_id_pk=_card_id(request))
        counter = CartItem.objects.filter(cart=cart).count()
        return {"counter": counter}
    except Cartmodel.DoesNotExist:
        return {"counter": 0}
    