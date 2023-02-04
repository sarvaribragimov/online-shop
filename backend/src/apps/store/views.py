from .models.product import Product
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from .models.category import Category
from django.core.paginator import Paginator, EmptyPage,\
                                    PageNotAnInteger


def product_list(request, category_slug=None):
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")
    if min_price and max_price:
        products = Product.objects.filter(price__gte=min_price,price__lte=max_price)

    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    page = request.GET.get("page")
    paginator = Paginator(products, 3)
    products = paginator.get_page(page)  
    return render(request,
                  'store.html',
                  {"page":page,
                  'categories': categories,
                  'products': products})
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                is_available=True)
    return render(request,
                'product-detail.html',
                {'product': product})                  