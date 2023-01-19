from django.urls import path

from .views import index_page,register,user_login

urlpatterns = [
    path("", index_page, name="index_page"),
    path('login/',user_login,name='login'),
    path('register/',register,name='register'),
]
