from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff', )
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Unregister the original User admin
admin.site.unregister(User)
# Register the customized one
admin.site.register(User, CustomUserAdmin)
