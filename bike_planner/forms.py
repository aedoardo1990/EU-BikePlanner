from django import forms
from .models import Contact, Trip


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "title", "content")


# form Trip
class TripForm(forms.ModelForm):
    
    class Meta:
        model = Trip
        fields = ["title", "start_date", "persons_number", "track", "additional_item"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        } # Datepicker created thanks to Stackoverflow

     


    