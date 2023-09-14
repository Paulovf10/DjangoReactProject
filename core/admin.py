from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at',)
    search_fields = ('name', 'email', 'subject')


admin.site.register(Contact, ContactAdmin)
