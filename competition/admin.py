from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ParticipantProfile, Competition, Submission
from django.db import models
from django.contrib.auth.models import User

# Inline Profile Info (for editing profile with user)
class ParticipantProfileInline(admin.StackedInline):
    model = ParticipantProfile
    can_delete = False

# Custom User Admin that shows Profile Inline
class CustomUserAdmin(BaseUserAdmin):
    inlines = (ParticipantProfileInline,)
    list_display = ('username', 'email', 'date_joined', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Register the custom User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register ParticipantProfile with its own detailed display
@admin.register(ParticipantProfile)
class ParticipantProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'school_name', 'parent_name', 'phone_number', 'selected_competition_date')
    search_fields = ('user__username', 'school_name', 'parent_name')
    list_filter = ('grade', 'selected_competition_date')

# Optional: Register other models
admin.site.register(Competition)
admin.site.register(Submission)

