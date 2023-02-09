from ...common.models import BaseModel
from django.db import models
from .product import Product
from ..managers import ProductVariansManager


class CategoryChoices(models.TextChoices):
    SIZE = "size"
    COLOR = "color"


class ProductVariants(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    variant_category = models.CharField(max_length=255, choices=CategoryChoices.choices, default=CategoryChoices.SIZE)
    variant_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = ProductVariansManager()

    class Meta:
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"

    def __str__(self):
        return f"{self.variant_category} - {self.variant_value}"