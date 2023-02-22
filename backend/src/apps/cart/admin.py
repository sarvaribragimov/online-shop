
from django.contrib import admin
from .models import Cartmodel,CartItem

@admin.register(Cartmodel)
class CartmodelAdmin(admin.ModelAdmin):
    list_display = ("user","cart_id_pk")
    list_filter = ("created_at",)
    date_hierarchy = ("created_at")

@admin.register(CartItem)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("cart","product","quantity","status","created_at")
    list_filter = ("created_at",)
    date_hierarchy = ("created_at")
    search_fields = ("product",)

    