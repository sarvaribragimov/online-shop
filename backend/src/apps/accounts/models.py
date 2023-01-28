# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .manager import AccoutManager
from django.contrib.auth.models import PermissionsMixin


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, db_index=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)

    # required
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "firstname"]

    objects = AccoutManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


# TODO Account Profile
