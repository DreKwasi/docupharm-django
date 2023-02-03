from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = ("email", "first_name", "username")
    readonly_fields = (
        "last_login",
        "date_joined",
    )
    ordering = (
        "-date_joined",
        "first_name",
    )
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "account",
        "professional_status",
        "gender",
        "registration_number",
        "created_date",
        "is_active",
    )
    readonly_fields = ("created_date",)
    ordering = ("-created_date",)


admin.site.register(Profile, ProfileAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "place_of_work",
        "location",
        "category",
    )
    readonly_fields = ("created_date",)
    ordering = ("-created_date",)


admin.site.register(Employer, EmployerAdmin)
