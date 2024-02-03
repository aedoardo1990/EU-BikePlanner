from django.contrib import admin
from .models import Route, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Route)
class RouteAdmin(SummernoteModelAdmin):
    """
    Enables Admin to manage routes in the Admin panel
    """
    list_display = ('title', 'status','created_on')
    search_fields = ['title']
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Enables Admin to check contact messages in the admin panel
    """
    list_display = ('title', 'name', 'email', 'created_on')
    search_fields = ['title', 'name']
    summernote_fields = ('content',)

