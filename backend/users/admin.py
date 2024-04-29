from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin # type: ignore
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email','user_type', )}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'user_type']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

