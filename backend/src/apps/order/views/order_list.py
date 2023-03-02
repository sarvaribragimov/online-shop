from django.shortcuts import render
from ..models import Order
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    return render(request,"order/order_list.html",{"orders":orders})