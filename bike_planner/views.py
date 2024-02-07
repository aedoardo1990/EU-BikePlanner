from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Route, Contact, Trip, Track
from .forms import ContactForm, TripForm

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


# Contact form - credits to https://github.com/WojtekKamilowski/CI_PP4_MPN
def get_user_data(request):
    """
    Retrieves details of user logged in
    """
    username = request.user.username
    email = request.user.email
    user = User.objects.filter(email=user_email, username=user_username).first()

    return user


class ContactDelivered(View):
    """
    Displays contact form for the user to send message to admin
    """
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email & name and inputs into relevant input
        """
        if request.user.is_authenticated:
            email = request.user.email
            name = request.user.username
            form = ContactForm(initial={"email": email, "name": name})
        else:
            form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        """
        Checks if the details are in valid format
        and then posts to database.
        """
        if request.method == "POST":
            form = ContactForm(data=request.POST)
            
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Message received! We will reply within 2 working days.")
                return render(request, "contact-received.html")
                
            return render(request, "contact.html", {"form": form})


class AddTrip(SuccessMessageMixin, generic.CreateView):
    """
    View to display the template to add a new bike trip
    """
    form_class = TripForm
    template_name = 'add-trip.html'
    success_message = "%(calculated_field)s was created successfully"

    def get_queryset(self):
        """Override get_queryset to filter by user"""
        return Trip.objects.filter(author=self.request.user)
    
    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the recipe title into the success message.
        credits: https://github.com/AliOKeeffe/PP4_My_Meal_Planner/tree/main
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class MyTrips(generic.ListView):
    """
    View to display the template to add a new bike trip
    """
    model = Trip
    form_class = TripForm
    template_name = 'my-trips.html'

    def get_queryset(self):
        """Override get_queryset to filter by user"""
        return Trip.objects.filter(author=self.request.user)


class TripDetails(View):
    """
    View to display the details of a trip
    """
    model = Trip
    
    def get(self, request, slug):
        """
        Retrives the trip details from the database
        """
        queryset = Trip.objects.all()
        trip = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "trip-details.html",
            {
                "trip": trip,
                "trip_form": TripForm()
            },
        )

    def post(self, request, slug):
        """
        This method is called when a POST request is made to the view
        via the trip form
        """
        queryset = Trip.objects.filter(status=1)
        trip = get_object_or_404(queryset, slug=slug)
        trip_form = TripForm(data=request.POST)
        
        return render(
            request,
            "trip-details.html",
            {
                "trip": trip,
                "trip_form": TripForm()
            },
        )
