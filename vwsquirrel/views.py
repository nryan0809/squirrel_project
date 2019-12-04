from django.shortcuts import render,get_object_or_404,redirect
from django.apps import apps
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import squ_model
from django.forms import ModelForm

def index(request):
    squirrels = squ_model.objects.all()
    context = {'squirrels': squirrels,
            }
    return render(request, 'vwsquirrel/index.html', context)


class SquForm(ModelForm):
    class Meta:
        model = squ_model
        fields = '__all__'

def add(request):
    if request.method == 'POST':
        form = SquForm(request.POST)
        form.save()
        return redirect('/sightings/')
    return render(request,'vwsquirrel/add.html')

