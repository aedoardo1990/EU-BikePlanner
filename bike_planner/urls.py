from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('routes/', views.RouteList.as_view(), name='routes'),
    path('route_details/<slug:slug>/', views.RouteDetails.as_view(), name='route_details'),
    path('contact/', views.ContactDelivered.as_view(), name="contact-us"),
    path('add-trip/', views.AddTrip.as_view(), name="add-trip"),
    path('my-trips/', views.MyTrips.as_view(), name="mytrips"),
    path('my-trips/<slug:slug/', views.TripDetails.as_view(), name='trip-details'),
    ]