from django.contrib import admin
from .models import Route, Contact, Track, Trip
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


@admin.register(Track)
class TrackAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change Routes from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Trip)
class TripAdmin(SummernoteModelAdmin):
    """
    Enables Admin to manage Trips in the Admin Panel
    """
    list_display = ('title', 'author', 'track', 'created_on')
    search_fields = ['title', 'track']
    list_filter = ('title', 'track','created_on')


