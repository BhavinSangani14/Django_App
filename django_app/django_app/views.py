from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
     
def course(request):
    return HttpResponse("This is a course page")

def courses(request, course_id):
    return HttpResponse(course_id)

def google(request):
    return render(request, "index.html")