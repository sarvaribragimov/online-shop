# Register your models here.
from django.contrib import admin

from .models import Order

# TODO configure admin panel
admin.site.register(Order)
