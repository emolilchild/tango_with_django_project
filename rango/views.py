from django.shortcuts import render

from django.http import HttpResponse

#this is one view
def index(request):
    #book says that each view must return a HttpResponse object
    return HttpResponse("Rango says hey there partner!")
