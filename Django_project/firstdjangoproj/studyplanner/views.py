from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
### Create functions or classes which mapps to urls

def index(request):
    return HttpResponse("Welcome to the Prathamesh's Study Planner setup")

def monday(request):
    return HttpResponse("Today I am learning Data Science")

def tuesday(request):
    return HttpResponse("Today I am learning Data engineering")


def weekly_timetable(request,day):
    text = ""
    if day == 'monday':
        text = "Today I am learning Data Science"
    elif day == 'tuesday':
        text =  "Today I am learning Data engineering"
    return HttpResponse(text)
