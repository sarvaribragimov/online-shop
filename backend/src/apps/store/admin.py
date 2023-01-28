from django.contrib import admin
from .models.product import Product
from .models.category import Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug','price','image','stock')
    list_filter = ('name','created_at','price')
    search_fields = ('name','description')
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug','description')


