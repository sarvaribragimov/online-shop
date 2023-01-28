from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.
from ...common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to="categories")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()
        # slug
    def get_absolute_url(self):
        return reverse("store:product_list",
                      args=[self.slug])
    