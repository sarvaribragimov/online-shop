from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category
from .models.review import Review
from .models.product import ProductImage


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)
    # autocomplete_fields = ("product",)
    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)


admin.site.register(ProductImage)
admin.site.register(Review, ReviewAdmin)

# TODO - configure admin
admin.site.register(Product)
admin.site.register(Category)
