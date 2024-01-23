from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ("name", "subject", "email", "sent_on")
    list_display = ("message_id", "name", "message", "sent_on")
    search_fields = ["email", "user"]