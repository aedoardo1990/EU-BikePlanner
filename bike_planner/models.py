from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
import datetime

STATUS = ((0, "Draft"), (1, "Published"))

# Route model for creating posts about EU Routes in Admin
class Route(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="routes"
    )
    route_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"


# Form model to render and handle forms in the admin panel
class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.title} | sent by {self.name}"


# Track model to create list of routes to select from in Trip model 
class Track(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    length = models.CharField(max_length=200, unique=False)
    countries_visited = models.CharField(max_length=200, unique=False)
    UNESCO_sites = models.CharField(max_length=200, unique=False)
    route_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.title}"


# Bike model to create list of bikes to select from in Trip model 
class Bike(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Clothes model to create list of clothes to select from in Trip model
class Clothes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Repair model to create list of repair tools to select from in Trip model
class Repair(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Bags model to create list of bags to select from in Trip model
class Bags(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Sleep model to create list of sleeping tools to select from in Trip model 
class Sleep(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Electric model to create list of electric tools to select from in Trip model 
class Electric(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Toilet model to create list of toiletries to select from in Trip model
class Toilet(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Cook model to create list of cooking tools to select from in Trip model 
class Cook(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


# Trip Model for creating a new trip
class Trip(models.Model):
    """
    Model for trip details
    """
    title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField()
    slug = AutoSlugField(populate_from='title')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mytrips")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    persons_number = models.IntegerField()
    bike_type = models.ForeignKey(Bike, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    repair_kit = models.ForeignKey(Repair, on_delete=models.CASCADE)
    bags = models.ForeignKey(Bags, on_delete=models.CASCADE)
    sleeping_kit = models.ForeignKey(Sleep, on_delete=models.CASCADE)
    electronics = models.ForeignKey(Electric, on_delete=models.CASCADE)
    toiletries = models.ForeignKey(Toilet, on_delete=models.CASCADE)
    cooking_kit = models.ForeignKey(Cook, on_delete=models.CASCADE)
    additional_items = models.CharField(max_length=200, unique=False)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        name = str(self.user.username)
        return name
    
    def get_absolute_url(self):
        """Get url after user adds/edits trip"""
        return reverse('trip-details', kwargs={'slug': self.slug})
    
    def __str__(self):
        return f"{self.title}"
    
    

