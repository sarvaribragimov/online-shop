from django.contrib.auth import get_user_model
from django.db import models

from ..cart.models import CartItem
from ..common.models import BaseModel,Region,City
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey
User = get_user_model()

class OrderStatus(models.TextChoices):
    NEW = "NEW", "Новый"
    IN_PROGRESS = "IN_PROGRESS", "В обработке"
    DONE = "DONE", "Выполнен"
    CANCELED = "CANCELED", "Отменен"

class Order(BaseModel):
    order_number = models.CharField(max_length=255, unique=True)  # date+order_id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    first_name = models.CharField(_('first_name'),max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,blank=True)

    cities = ChainedForeignKey(
        City,
        chained_field="region",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.SET_NULL,
        null=True
    )
    
    address = models.CharField(max_length=255)
    order_note = models.TextField(blank=True, null=True)  # TODO RichTextField
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ip = models.CharField(max_length=255)
    status = models.CharField(_("status"),max_length=255, 
    choices=OrderStatus.choices, default=OrderStatus.NEW)
    cart_items = models.ManyToManyField(CartItem, related_name="orders")


    

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        ordering = ['-created_at']
        verbose_name  = "Order"
        verbose_name_plural = "Orders"
        
                
        

