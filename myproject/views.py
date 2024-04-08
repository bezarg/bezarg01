# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("hello world! I'm home.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("my about page.")
    return render(request, 'about.html')