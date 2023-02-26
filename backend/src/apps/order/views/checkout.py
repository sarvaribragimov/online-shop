from django.shortcuts import render
from ...cart.models import Cart,CartItem,StatusChoices
from django.db.models import F ,Sum
from ...common.get_cart_id import _cart_id
from decimal import Decimal
from ..forms import OrderForm

def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    else:
        cart = CartItem.objects.filter(cart_id_pk=_cart_id(request)).first()
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    # annotate
    cart_item = cart_items.annotate(total_price=F("product__price") * F("quantity"))
    total_price = cart_item.aggregate(Sum("total_price"))
    total_price = total_price["total_price__sum"] or 0

    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price

    grand_total = total_price + delevery
    form = OrderForm()
    context = {"cart_items": cart_items, "total_price": total_price,
             "delevery": delevery,"form":form,   "grand_total": grand_total}
    return render(request, "order/checkout.html", context)

