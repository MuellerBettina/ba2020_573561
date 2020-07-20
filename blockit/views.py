from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'calendar.html'





def home(request):
    return render(request, 'blockit/home.html', {})

def about(request):
    return render(request, 'blockit/about.html', {})