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

def detail(request,Unique_Squirrel_ID):
    details = get_object_or_404(squ_model,Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        if 'delete' in request.POST:
            details.delete()
        else:
            details = SquForm(instance=details,data=request.POST)
            if details.is_valid():
                 details.save()
        return redirect('/sightings/')
    return render(request, 'vwsquirrel/detail.html',{'details':details})
