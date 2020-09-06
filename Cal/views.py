from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime
import datetime
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
        week.append(datetime.datetime.strftime((first_day+delta), "%d-%B"))
    return render(request, "Cal/weeklycalendar.html", {'events': events, 'week': week, 'year': year, 'range7': range(7), 'range24': range(24), 'month': month, 'way': way})

@login_required()
def get_event(request, id):
    if (request.method != 'GET'):
        return HttpResponseNotFound()
    try:
        data = Event.objects.get(id=id)
        data = Event.objects.filter(title=data.title, the_start_time=data.the_start_time,
                                      the_end_time=data.the_end_time).first()
    except:
        return HttpResponseNotFound()
    data = {'id':data.id, 'title':data.title, 'the_date':data.the_date.__str__(), 'the_start_time':data.the_start_time.__str__(),
            'the_end_time':data.the_end_time.__str__(), 'color':data.color}
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required()
def delete_event(request, id):
    if(request.method != 'GET'):
        return HttpResponseNotFound()
    try:
        Event.objects.get(id=id).delete()
        return HttpResponse()
    except:
        return HttpResponseNotFound()




@login_required()
def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            start_time = request.POST['starting_time']
            end_time = request.POST['ending_time']
            starting_time_object = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M')
            ending_time_object = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M')
            the_start_time = starting_time_object.time()
            the_end_time = ending_time_object.time()
            the_date = starting_time_object.date()
            new_event = Event(title=request.POST['title'], user=user, the_start_time=the_start_time, the_end_time=the_end_time, color=request.POST['color'], the_date=the_date, start_time=start_time, end_time=end_time)
            new_event.save()
            return redirect("/timeblocks")
    else:
        form = EventForm()
    return render(request, 'Cal/addEvent.html', {'form': form})