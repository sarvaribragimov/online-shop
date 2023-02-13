# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


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
    list_display = ("thumbnail","user", "city", "state", "address")
    list_filter = ("city", "state")
    list_display_links = ("user", "city", "state", "address")

    def thumbnail(self, object):
        if object.profile_pic:
            return format_html(
                f'<img src="{object.profile_pic.url}" width="80px" height="80px" style="border-radius: 50px;" />'
            )
        else:
            return format_html(
                '<img src="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png" width="40" style="border-radius: 50px;" />'
            )

    thumbnail.short_description = "Profile Pic"

    def set_default_city(self,request,queryset):
        queryset.update(city="Tashkent city")

    set_default_city.short_description = "set default Tashkent city"

    actions = ["set_default_city"]


admin.site.register(UserProfile, UserProfileAdmin)
