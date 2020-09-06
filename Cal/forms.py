from django import forms
from .models import Event
from timeblocks.widgets import DateTimePickerInput

class EventForm(forms.ModelForm):

    starting_time = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=DateTimePickerInput())
    ending_time = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=DateTimePickerInput())

    class Meta:
        model = Event
        fields = ['title', 'starting_time', 'ending_time', 'color']