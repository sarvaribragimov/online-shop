from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category
from .models.review import Review
from .models.product import ProductImage
from .models.variants import ProductVariants
import admin_thumbnails

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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)
    # autocomplete_fields = ("product",)
    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)



admin.site.register(Review, ReviewAdmin)

# TODO - configure admin

admin.site.register(Category)
admin.site.register(ProductVariants)
