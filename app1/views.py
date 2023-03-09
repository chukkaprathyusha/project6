from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse("Dhoni is the best finisher in the world")

def rohith(request):
    return HttpResponse("rohith is the best batsman")

