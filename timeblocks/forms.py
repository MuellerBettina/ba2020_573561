from django import forms

from Cal.models import Event
from .models import TimeBlockList
from .widgets import DateTimePickerInput

class TimeBlockForm(forms.ModelForm):
    class Meta:
        model = TimeBlockList
        fields = ['name', 'description', 'length', 'color']


class DateForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=DateTimePickerInput())

    class Meta:
        model = Event
        fields = ('date',)
