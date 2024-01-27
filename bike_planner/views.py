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
    model = Route
    queryset = Route.objects.all().order_by("created_on")
    template_name = 'routes.html'


# class inspired from https://github.com/AliOKeeffe/PP4_My_Meal_Planner/tree/main
class RouteDetails(View):
    """
    View used to display the route details.
    """
    def get(self, request, slug):
        """
        Retrieves the route from the database
        """
        queryset = Route.objects.all()
        route = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "route_details.html",
            {"route": route,},
        )

