from datetime import timedelta, date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import EventForm, ContactForm
from .utils import Calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.views import generic
from .models import *
from django.core.mail import send_mail
import calendar



def index(request):
    return HttpResponse('hello')


class CalendarView(generic.ListView):
    model = Action
    template_name = 'blockit/calendar.html'
    #success_url = reverse_lazy("calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=False)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Action()
    if event_id:
        instance = get_object_or_404(Action, pk=event_id)
    else:
        instance = Action()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})

def home(request):
    return render(request, 'blockit/home.html', {})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']

        # send an email
        send_mail(
            subject + first_name + last_name,
            body,
            email,
            ['MuellerBettina@pm.me'],
        )

        return render(request, 'blockit/contact.html', {'first_name': first_name})

    else:
        return render(request, 'blockit/contact.html', {'form': form})


def about(request):
    return render(request, 'blockit/about.html', {})
