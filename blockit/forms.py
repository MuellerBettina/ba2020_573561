from django.forms import ModelForm, DateInput
from django import forms
from blockit.models import Action

class EventForm(ModelForm):
  class Meta:
    model = Action
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class ContactForm(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField(label='E-Mail')
  subject = forms.CharField(required=False)
  body = forms.CharField(widget=forms.Textarea)




