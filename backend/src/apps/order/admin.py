from django.contrib import admin
from .models import Order

class OrderItem(admin.TabularInline):
    model = Order
    raw_id_fields = ["product"]
    extra = 2

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id",'first_name', 'last_name', 'regions', 
                    'phone_number', 'city',"address","order_note","status"]   

    