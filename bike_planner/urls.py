from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    #path('routes/', views.RouteList.as_view(), name='routes'),
]