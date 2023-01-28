from django.urls import path

from .views.index import index_page
from .views.register import register
from .views.login import login
from .views.logout_user import logout_user
from .views.activate import activate
from .views.reset_password import forgot_password, validate_password

urlpatterns = [
    path("", index_page, name="index_page"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout_user, name="logout_user"),
    path("activate/<uidb64>/", activate, name="activate"),
    # reset password
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("verify-password/<uidb64>/", validate_password, name="validate_password"),
]
