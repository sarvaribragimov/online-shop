from .models import Cartmodel, CartItem


def counter(request):
    # TODO cache
    cart, created = Cartmodel.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    counter = cart_items.count()
    # TODO user  Sum aggregation
    return {"counter": counter}
