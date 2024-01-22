from django.shortcuts import render
from django.views import generic, View

# Create your views here.
class Homepage(generic.TemplateView):
    """
    View to display the Homepage
    """
    template_name = 'bike_planner/index.html'