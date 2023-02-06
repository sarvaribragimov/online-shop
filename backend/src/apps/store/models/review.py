from django.db import models
from ...common.models import BaseModel
from ...accounts.models import Account
from .product import Product


class Review(BaseModel):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    ip = models.GenericIPAddressField()
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]