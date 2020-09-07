import datetime
from datetime import timedelta

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView
import timeblocks
from Cal.models import Event
from timeblocks.forms import TimeBlockForm, DateForm
from timeblocks.models import TimeBlock, TimeBlockList
from . import models

@login_required
def addTimeBlock(request):
    form = TimeBlockForm()
    if request.method == 'POST' and 'save' in request.POST:
        print("schedule later was pressed")
        form = TimeBlockForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            new_timeblock = TimeBlockList(name=request.POST['name'], user=user, length=request.POST['length'], description=request.POST['description'], color=request.POST['color'])
            new_timeblock.save()
            return redirect("/timeblocks")
        else:
            form = TimeBlockForm()
    elif request.method == 'POST' and 'save and schedule' in request.POST:
        print("schedule now was pressed")
        form = TimeBlockForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            new_timeblock_to_be_scheduled = TimeBlockList(name=request.POST['name'], user=user, length=request.POST['length'], description=request.POST['description'], color=request.POST['color'])
            new_timeblock_to_be_scheduled.save()
            block_id = new_timeblock_to_be_scheduled.id
            return HttpResponseRedirect(reverse('scheduleTimeBlock', kwargs={'block_id': block_id}))
        else:
            form = TimeBlockForm()
    return render(request, 'timeblocks/timeblocks.html', {'form': form})

@login_required
def deleteTimeBlock(request, block_id):
    TimeBlockList.objects.get(id=block_id).delete()
    timeblocklist = TimeBlockList.objects.all()

    return render(request, 'timeblocks/timeblocklist.html', {"timeblocklist": timeblocklist})


class ScheduleTimeBlock(CreateView):
    form_class = DateForm
    template_name = 'timeblocks/pickdatetime.html'

    def post(self, request, block_id):
        timeblock = TimeBlockList.objects.get(id=block_id)

        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            starting_time = request.POST['date']
            starting_time_object = datetime.datetime.strptime(starting_time, '%Y-%m-%d %H:%M')
            color = timeblock.color
            just_date = starting_time_object.date()
            minutes_to_add = timeblock.length
            ending_time = starting_time_object + timedelta(minutes=minutes_to_add)
            just_start_time = starting_time_object.time()
            just_end_time = ending_time.time()
            new_event = Event(title=timeblock.name, user=user, start_time=request.POST['date'], end_time=ending_time,
                              the_date=just_date, the_start_time=just_start_time, the_end_time=just_end_time,
                              color=color)
            new_event.save()
            timeblock.delete()
            return redirect('timeBlockList')
        else:
            return render(request, self.template_name, {'form': form})



@login_required
def showTimeBlock(request, block_id):

    timeblock = TimeBlockList.objects.get(id=block_id)

    return render(request, 'timeblocks/timeblockview.html', {"timeblock": timeblock})


@login_required
def timeBlockList(request):

    timeblocklist = TimeBlockList.objects.all()

    if "save" in request.POST:
        name = request.POST["name"]
        description = request.POST["description"]
        length = request.POST["length"]
        user = User.objects.get(id=request.user.id)
        Block = TimeBlockList(user=user, description=description, name=name, length=length)
        Block.save()
        return redirect("/timeblocks")

    return render(request, 'timeblocks/timeblocklist.html', {"timeblocklist": timeblocklist})
