from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Roles", {
            "fields": ("is_student", "is_instructor"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Roles", {
            "fields": ("is_student", "is_instructor"),
        }),
    )

    list_display = ("username", "email", "is_student", "is_instructor", "is_staff")

    list_filter = ("is_student", "is_instructor", "is_staff")