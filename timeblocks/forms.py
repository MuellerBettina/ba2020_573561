from django import forms
from .models import TimeBlockList

class TimeBlockForm(forms.ModelForm):
    class Meta:
        model = TimeBlockList
        fields = ['name', 'description', 'length']