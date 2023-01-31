from django.urls import path

from .views import product_list,product_detail

urlpatterns = [
    path("list/", product_list, name="product_list"),
    path('<slug:category_slug>/',product_list,name="product_list"),
    path('<int:id>/<slug:slug>/',product_detail,name='product_detail')
]
