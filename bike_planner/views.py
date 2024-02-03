from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Route, Contact
from .forms import ContactForm

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


# Contact form
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
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            # messages.success(request, "Your message has been sent")
            return render(request, "contact-received.html")

        return render(request, "contact.html", {"form": form})
    
