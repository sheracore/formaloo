from django.contrib import admin
from .models import App, VerificationStatus

def mark_as_verified(modeladmin, request, queryset):
    queryset.update(verification_status=VerificationStatus.VERIFIED)
mark_as_verified.short_description = 'Mark selected apps as Verified'

def mark_as_rejected(modeladmin, request, queryset):
    queryset.update(verification_status=VerificationStatus.REJECTED)
mark_as_rejected.short_description = 'Mark selected apps as Rejected'

def mark_as_pending(modeladmin, request, queryset):
    queryset.update(verification_status=VerificationStatus.PENDING)
mark_as_pending.short_description = 'Mark selected apps as Pending'

class AppAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'verification_status', 'category', 'created_at', 'updated_at']
    actions = [mark_as_verified, mark_as_rejected, mark_as_pending]

admin.site.register(App, AppAdmin)