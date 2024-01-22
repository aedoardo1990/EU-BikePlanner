from django.db import models
from django.contrib.auth.models import User


# Contact Model inspired from https://github.com/WojtekKamilowski/CI_PP4_MPN/tree/main
class Contact(models.Model):
    """
    Contact model class for Contact form
    """
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200, default="")
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return f"{self.subject} | sent by {self.name}"