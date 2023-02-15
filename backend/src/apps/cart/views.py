from django.shortcuts import render, redirect,get_object_or_404
from .models import Cartmodel, CartItem, StatusChoices
from ..store.models.variants import ProductVariants
from django.db.models import Sum, F
from django.db import models
from decimal import Decimal
from .forms import CartAddproductForm
from ..store.models.product import Product
from .cart import Cart
from django.views.decorators.http import require_POST
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # product_id = request.POST.get("product_id")
    form = CartAddproductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(f" cleaned date  e ={cd}")
        cart.add_to_cart(product=product,
        quantity=cd['quantity'],)
    return redirect('cart:cart_detail')
 
def add_cart(request):
    """
    #TODO add to cart
    post:
        product id
        variations if
        quantity 1

    """
    # get product variations
    if request.method != "POST":
        return render(request, "store/cart_items.html", {"cart_items": None})
    product_id = request.POST.get("product_id")
    size = request.POST.get("size")
    color = request.POST.get("color")
    # check if cart exists
    cart, created = Cartmodel.objects.get_or_create(user=request.user)

    variations = ProductVariants.objects.filter(product_id=product_id, variant_value__in=[size, color])
    print(variations)
    # check if cart item exists
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

    # add variations to cart item
    for variation in variations:
        cart_item.variations.add(variation)

    cart_item.save()

    return redirect("cart:cart")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.dele(product)
    return redirect('cart:cart_detail')


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/cart_items.html', {'cart': cart})

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddproductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/cart_items.html', {'cart': cart})    