from django.shortcuts import render
from datetime import date, timedelta, datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

    week = []
    year = first_day.year
    month = first_day.month
    for i in range(7):
        delta = timedelta(days=i)
        week.append(datetime.strftime((first_day+delta), "%d-%B"))
    return render(request, "Cal/weeklycalendar.html", {'week': week, 'year': year, 'range7' : range(7), 'range24': range(24), 'month': month, 'way': way })