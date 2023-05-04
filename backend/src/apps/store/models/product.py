from django.db import models
from django.utils.translation import gettext_lazy as _

# Avg, Count, Min, Sum
from django.db.models import Avg

# Create your models here.
from ...common.models import BaseModel
from ...common.file_renamer import PathAndRename
from django.utils.text import slugify
from django.urls import reverse

from ...accounts.models import Account

from .category import Category

# products/file_{id}_{hex4}.{ext}
path_and_rename = PathAndRename("products")

# Product model
class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, db_index=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True, help_text="Is product available?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", blank=True, null=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]

    @property
    def get_absolute_url(self):
        return reverse("store:product_detail_view", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save()
    
    def averageReview(self):
        reviews = Review.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    @property
    def average_rating(self):
        reviews = self.reviews.filter(status=True).aggregate(Avg("rating"))
        return float(reviews["rating__avg"]) if reviews["rating__avg"] else 0

def validate_desc(value):
    # TODO move to forms.py
    # list of bad words
    bad_words = ["yomon","bad"]
    # check if bad words in review description
    if any(word in value for word in bad_words):
        raise ValidationError("Bad words in review description")




class Review(BaseModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    desc = models.TextField(validators=[validate_desc], help_text="Review haqida izoh")
    status = models.BooleanField(default=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    rating = models.FloatField(null=True, blank=True)
    # reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=path_and_rename)

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
