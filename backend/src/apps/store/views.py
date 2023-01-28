from .models.product import Product
from django.views.generic.list import ListView

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "store.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(is_available=True)


product_list_view = ProductListView.as_view()

from django.shortcuts import render, get_object_or_404
from .models.category import Category

def product_list(request, category_slug=None):
    # Category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'store.html',
                  {'category': category,
                  'categories': categories,
                  'products': products})
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                'store:product_detail.html',
                {'product': product})                  