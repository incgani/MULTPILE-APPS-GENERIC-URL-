from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view_App_01(request):
    return HttpResponse('<h1>This Is The first_view_App_01</h1>')
def Second_view_App_01(request):
    return HttpResponse('<h1>This Is The Second_view_App_01</h1>')


