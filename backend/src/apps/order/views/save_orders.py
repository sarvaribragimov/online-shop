from ..forms import OrderForm
from django.shortcuts import redirect
from ...cart.models import CartItem,StatusChoices
from time import time
from django.db.models import F,Sum

def save_orders(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_items = CartItem.objects.filter(cart__user=request.user, status=StatusChoices.ACTIVE)
            total_price = cart_items.aggregate(total_price=Sum(F("product__price") * F("quantity")))["total_price"] 
            print(total_price)
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            # current time in seconds + user id
            order.order_number = str(int(time())) + str(request.user.id)
            order.total_price = total_price
            order.ip = request.META.get("REMOTE_ADDR")
            order.save()

            # add cart items to order
            order.cart_items.set(cart_items)

            # Update cart items status clear cart
            cart_items.update(status=StatusChoices.INACTIVE)

            # save order
            order.save()

            return redirect("order:order_list")
    return redirect("order:checkout")
                
