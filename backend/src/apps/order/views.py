from django.shortcuts import render,get_object_or_404
from .models import OrderItem
from .forms import OrderForm
from ..cart.models import Cartmodel,CartItem,StatusChoices


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            first_name = form.cleaned_data.get("first_name")
            first_name = form.cleaned_data.get("first_name")
    
    
    return render(request,
                'order/order.html',
                {'cart': cart})   