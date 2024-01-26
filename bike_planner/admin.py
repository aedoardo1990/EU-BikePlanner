from django.contrib import admin
from .models import Route
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Route)
class RouteAdmin(SummernoteModelAdmin):
    """
    Enables Admin to manage Routes in the Admin panel
    """
    list_display = ('title', 'status','created_on')
    search_fields = ['title']
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
