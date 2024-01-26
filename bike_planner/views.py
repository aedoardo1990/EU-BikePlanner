from django.shortcuts import render
from django.views import generic, View
from .models import Route

# Create your views here.
class Homepage(generic.TemplateView):
    """
    View to display the Homepage
    """
    template_name = 'index.html'


class RouteList(generic.ListView):
    """
    View is used to display all routes in the routes page
    """
    queryset = Route.objects.all()
    template_name = 'routes.html'