from django import forms
from .models import Contact, Trip
from datetime import datetime
from crispy_forms.helper import FormHelper


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "title", "content")


class DateInput(forms.DateInput):
    input_type = "date"


# form Trip
class TripForm(forms.ModelForm):
    
    class Meta:
        model = Trip
        fields = ["title", "start_date", "persons_number", "track", "additional_item"]
        widgets = {
            'start_date':DateInput(attrs={'class': 'datepicker','data-date-format': 'yyyy/mm/dd',}),
            }

     


    