from django import forms
from .models import Contact, Trip
from datetime import date

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "title", "content")


# form Trip
class TripForm(forms.ModelForm):
    
    class Meta:
        model = Trip
        fields = ["title", "start_date", "route", "persons_number", "bike_type", "clothes", "repair_kit", "bags", "sleeping_kit", "electronics", "toiletries", "cooking_kit", "additional_items"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        } # Datepicker created thanks to Stackoverflow
    
    # code below to not accept start date in the past - credits: https://copyprogramming.com/howto/django-how-to-prevent-to-accept-future-date
    def clean_start_date(self):
        date = self.cleaned_data.get('start_date')

        if date < date.today():
            raise forms.ValidationError('The date must be today or in the future.')

        return date


    