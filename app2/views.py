from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse("virat is the best captain")

def rahul(request):
    return HttpResponse("rahul is best allrounder")    