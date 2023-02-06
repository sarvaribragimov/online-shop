from ..models.product import Product
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from ..models.category import Category
from ..models.review import Review
from django.db.models import Q
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

# def product_detail_view(request, category_slug, product_slug):
#     product = Product.objects.get(category__slug=category_slug, slug=product_slug)
#     product_reviews = Review.objects.filter(product=product)
#     product_images = ProductImage.objects.filter(product=product)
#     context = {
#         "product": product,
#         "product_reviews": product_reviews,
#         "product_images": product_images,
#     }
#     return render(request, "store/product_detail.html", context)

def product_detail(request, id, slug):

    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                is_available=True)
    product_reviews = product.reviews.filter(status=True)
    context = {
        "product": product,
        "product_reviews": product_reviews,
        
    }                            
    return render(request,'product-detail.html',context)   

def search(request):
    products = Product.objects.filter(is_available=True)
    if "q" in request.GET:
        if q:=request.GET["q"]:
            products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))

    product_count=products.count()
    context = {
        'products':products,
        'product_count':product_count,
    }
    return render(request,"store.html",context)