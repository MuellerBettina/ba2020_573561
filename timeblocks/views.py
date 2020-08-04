from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from timeblocks.forms import TimeBlockForm
from timeblocks.models import TimeBlock, TimeBlockList
from . import models

@login_required
def addTimeBlock(request):
    if request.method == 'POST':
        form = TimeBlockForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            new_timeblock = TimeBlockList(name=request.POST['name'], user=user, length=request.POST['length'], description=request.POST['description'])
            new_timeblock.save()
            return redirect('blockit:blockit-home')
    else:
        form = TimeBlockForm()
    return render(request, 'timeblocks/timeblocks.html', {'form': form})

@login_required
def deleteTimeBlock(request, block_id):
    TimeBlockList.objects.get(id=block_id).delete()
    timeblocklist = TimeBlockList.objects.all()

    return render(request, 'timeblocks/timeblocklist.html', {"timeblocklist": timeblocklist})

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
