from django.urls import path
from .views import Home

urlpatterns = [
    path('accounts/',Home,name='home'),
]