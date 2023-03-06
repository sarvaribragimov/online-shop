from django.views.generic.base import TemplateView
from django.shortcuts import render
from ...store.models.product import Product,Category
# Create your views here.


    

def index_page(request, category_slug=None):
    products = Product.objects.filter(is_available=True)  
    print(products)
    
    return render(request, "index.html", {"products": products})
  

