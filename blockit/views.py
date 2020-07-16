from django.shortcuts import render

def home(request):
    return render(request, 'blockit/home.html', {})

def about(request):
    return render(request, 'blockit/about.html', {})