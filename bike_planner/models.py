from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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


