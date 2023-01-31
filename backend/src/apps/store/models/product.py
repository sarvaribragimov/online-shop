from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.
from ...common.models import BaseModel
from ...common.file_renamer import PathAndRename
from django.utils.text import slugify

from .category import Category

# products/file_{id}_{hex4}.{ext}
path_and_rename = PathAndRename("products")

# Product model
class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, db_index=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=path_and_rename)
    stock = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True, help_text="Is product available?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('store:product_detail',
                        args=[self.id,self.slug])
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()
