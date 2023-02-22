from django.contrib import admin
from .models import Order,OrderItem

class OrderItem(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
    extra = 2

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id",'first_name', 'last_name', 'regions', 
                    'phone_number', 'city',"address"]   

    inlines = [OrderItem]