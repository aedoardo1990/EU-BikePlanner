from django.contrib import admin
from .models import Route, Contact, Trip, Bike, Clothes, Repair, Bags, Sleep, Electric, Toilet, Cook
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


@admin.register(Trip)
class TripAdmin(SummernoteModelAdmin):
    """
    Enables Admin to manage Trips in the Admin Panel
    """
    list_display = ('title', 'user', 'route', 'created_on')
    search_fields = ['title', 'route']
    list_filter = ('title', 'route','created_on')


@admin.register(Bike)
class BikeAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change bike from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Clothes)
class ClothesAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change clothing from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Repair)
class RepairAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change repair kit from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Bags)
class BagsAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change bag from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Sleep)
class SleepAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change sleep kit from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Electric)
class ElectricAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change electronics from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Toilet)
class ToiletAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change toiletries from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']


@admin.register(Cook)
class CookAdmin(SummernoteModelAdmin):
    """
    Enables Admin to change cook kit from option lists in the Add Trip Form
    """
    list_display = ('title', 'created_on')
    search_fields = ['title']