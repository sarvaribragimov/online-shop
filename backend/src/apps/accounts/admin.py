# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile


class AccountUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    list_display_links = ("username", "email", "phone_number")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "phone_number", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "firstname",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(Account, AccountUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "address")
    list_filter = ("city", "state")
    list_display_links = ("user", "city", "state", "address")


admin.site.register(UserProfile, UserProfileAdmin)
