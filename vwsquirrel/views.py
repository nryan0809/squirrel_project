<<<<<<< HEAD
from django.shortcuts import render
from .models import squirrel_model
from django.http import HttpResponse

def index(request,x):
    return HttpResponse(squirrel_model.objects.all())

=======
from django.shortcuts import render,get_object_or_404
from django.apps import apps
>>>>>>> 8226e84c9c6fad8e31d65a22447fa3d6d936159e
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import squirrel_model

def index(request):
    squirrels = squirrel_model.objects.all()
    context = {'squirrels': squirrels,
            }
    return render(request, 'vwsquirrel/index.html', context)
