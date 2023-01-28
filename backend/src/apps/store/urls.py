from django.urls import path

from .views import product_list_view,product_list,product_detail

urlpatterns = [
    path("list/", product_list_view, name="product_list_view"),
    path('<slug:category_slug>/',product_list,name="product_list"),
    path('<int:id>/<slug:slug>/',product_detail,name='product_detail')
]
