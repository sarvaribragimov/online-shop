from django.db import models


class ProductVariansManager(models.Manager):
    def colors(self):
        from .models.variants import CategoryChoices

        return self.filter(variant_category=CategoryChoices.COLOR)
    def sizes(self):
        from .models.variants import CategoryChoices
        return self.filter(variant_category=CategoryChoices.SIZE)