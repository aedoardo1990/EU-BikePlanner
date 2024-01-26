from django.shortcuts import render, get_object_or_404
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
    queryset = Route.objects.all().order_by("created_on")
    template_name = 'routes.html'

    def route_details(request, slug):
        queryset = Route.objects.filter(status=1)
        route = get_object_or_404(queryset, slug=slug)
        return render(request, "bike_planner/route_details.html", {"route": route},)
