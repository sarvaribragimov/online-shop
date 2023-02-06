from django.urls import path

from .views.product import product_list,product_detail,search 
from .views.review import add_review

urlpatterns = [
    path("search/",search,name='search'),
    path("list/", product_list, name="product_list"),
    path('<slug:category_slug>/',product_list,name="product_list"),
    path('<int:id>/<slug:slug>/',product_detail,name='product_detail'),
    
    path("review/add/<int:product_id>", add_review, name="add_review"),
]
