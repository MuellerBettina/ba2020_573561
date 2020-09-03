from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Cal.models import Event
from Cal.forms import EventForm
import json

def convert_data(events_object):
    data = []
    for i in events_object:
        data.append({'id':i.id, 'title':i.__str__(), 'color':i.color, 'the_date':str(i.the_date.day),
                     'the_start_time':str(int(str(i.the_start_time)[0:2])), 'the_end_time':str(int(str(i.the_end_time)[0:2]))})
    return data

@login_required()
def calendar(request):
    first_day = date.today().weekday()
    first_day = timedelta(days=first_day)
    first_day = date.today() - first_day
    way = [-1,1] #you can either go forward or backwards
    try:
        way[0] = int(request.GET['n']) - 1
        way[1] = int(request.GET['n']) + 1
        delta = timedelta(days=int(request.GET['n']) * 7)
        first_day = first_day + delta #neuer erster Tag ist der alte Tag plus Zeitspanne
    except:
        pass
    events = Event.objects.filter(user=request.user, the_date__range=(first_day, first_day+timedelta(days=6)))
    events = convert_data(events)
    week = []
    year = first_day.year
    month = first_day.month
    for i in range(7):
        delta = timedelta(days=i)
        week.append(datetime.strftime((first_day+delta), "%d-%B"))
    return render(request, "Cal/weeklycalendar.html", {'events': events, 'week': week, 'year': year, 'range7': range(7), 'range24': range(24), 'month': month, 'way': way})

def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            new_event = Event(title=request.POST['title'], user=user, the_start_time=request.POST['the_start_time'], the_end_time=request.POST['the_end_time'], color=request.POST['color'])
            new_event.save()
            return redirect("/timeblocks")
    else:
        form = EventForm()
    return render(request, 'Cal/addEvent.html', {'form': form})