from django import forms
from .models import Contact, Trip

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "title", "content")


# form Trip TO BE DEVELOPED
class TripForm(forms.ModelForm):
    
    class Meta:
        model = Trip
        fields = ("title", "persons_number", "track", "additional_item")
     


    