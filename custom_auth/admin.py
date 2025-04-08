from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'phone', 'address', 'birth_date', 'is_verified',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'address', 'birth_date', 'is_verified')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'address', 'birth_date', 'is_verified')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)