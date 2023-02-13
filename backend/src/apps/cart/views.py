from django.shortcuts import render, redirect,get_object_or_404
from .models import Cartmodel, CartItem, StatusChoices
from ..store.models.variants import ProductVariants
from django.db.models import Sum, F
from django.db import models
from decimal import Decimal
from .forms import CartAddproductForm
from ..store.models.product import Product
from .cart import Cart



def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # product_id = request.POST.get("product_id")
    form = CartAddproductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(f" cleaned date  e ={cd}")
        cart.add(product=product,
        quantity=cd['quantity'],
        override_quantity=cd['override'])
    return redirect('cart:cart')

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


def cart(request):
    cart = Cartmodel.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    total_price = cart_items.aggregate(
        total_price=Sum(
            F("product__price") * F("quantity"), output_field=models.DecimalField(max_digits=10, decimal_places=2)
        )
    )["total_price"]
    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price
    grand_total = total_price + delevery

    context = {"cart_items": cart_items, "total_price": total_price, "delevery": delevery, "grand_total": grand_total}
    return render(request, "cart/cart_items.html", context)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddproductForm(initial={
                'quantity': item['quantity'],
                'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})