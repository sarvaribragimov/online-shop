import admin_thumbnails
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models.category import Category
from .models.product import Product, ProductImage
from ..store.models.product import Review
from .models.variants import ProductVariants

# Register your models here.


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ("id","name","created_at")

@admin.register(Category)
class CategoryModelAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ("name", "slug","created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
    prepopulated_fields = {"slug": ("name",)}
    


@admin_thumbnails.thumbnail("image")
class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name",)
    raw_id_fields = ("category",)
    date_hierarchy = "created_at"
    list_editable = ("price", "stock")
    prepopulated_fields = {"slug": ("name",)}  # TODO - add slug field all models
    inlines = [ProductImageModelAdmin]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user","rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)
    # autocomplete_fields = ("product",)
    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)

@admin.register(ProductVariants)
class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ("product", "variant_category", "variant_value", "is_active")
    list_filter = ("variant_value", "created_at")
    search_fields = ("product",)
    date_hierarchy = "created_at"
 
 
 