from django.shortcuts import render
from .models import squirrel_model
from django.http import HttpResponse

def index(request,x):
    return HttpResponse(squirrel_model.objects.all())

# Create your views here.
