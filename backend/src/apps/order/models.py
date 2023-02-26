from django.contrib.auth import get_user_model
from django.db import models

from ..cart.models import CartItem
from ..common.models import BaseModel


User = get_user_model()

class OrderStatus(models.TextChoices):
    NEW = "NEW", "Новый"
    IN_PROGRESS = "IN_PROGRESS", "В обработке"
    DONE = "DONE", "Выполнен"
    CANCELED = "CANCELED", "Отменен"

class Order(BaseModel):
    order_number = models.CharField(max_length=255, unique=True)  # date+order_id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    regions = models.CharField(max_length=255)  # TODO Model Region
    city = models.CharField(max_length=255)  # TODO Model City
    address = models.CharField(max_length=255)
    order_note = models.TextField(blank=True, null=True)  # TODO RichTextField
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ip = models.CharField(max_length=255)
    status = models.CharField(max_length=255, 
    choices=OrderStatus.choices, default=OrderStatus.NEW)
    cart_items = models.ManyToManyField(CartItem, related_name="orders")


    

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        ordering = ['-created_at']
        verbose_name  = "Order"
        verbose_name_plural = "Orders"
        
                
        

