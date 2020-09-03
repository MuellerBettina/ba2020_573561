from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'the_start_time', 'the_end_time', 'the_date', 'color']