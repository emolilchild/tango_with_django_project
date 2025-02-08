from django.shortcuts import render

from django.http import HttpResponse

#this is one view
def index(request):
    #book says that each view must return a HttpResponse object
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

#chapter 3 exercise
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
