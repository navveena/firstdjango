from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def naveena(request):
    return HttpResponse("<h1>welcome</h1>")

def naveena2(request):
    return HttpResponse("<h4>welcome i am naveena</h4>")