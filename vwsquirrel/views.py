from django.shortcuts import render,get_object_or_404
from django.apps import apps
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import squ_model
<<<<<<< HEAD
from django.forms import ModelForm

class SightingForm(ModelForm):
    class Meta:
        model = squ_model
        fields = '__all__'
=======
>>>>>>> b7b37774823c9a767613a3f113c220ce48543b8f

def index(request):
    squirrels = squ_model.objects.all()
    context = {'squirrels': squirrels,
            }
    return render(request, 'vwsquirrel/index.html', context)

def detail(request,Unique_Squirrel_ID):
    details = squ_model.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        details.Longitude=request.POST['Longitude']
        details.Latitude=request.POST['Latitude']
        details.Shift=request.POST['Shift']
        details.Date=request.POST['Date']
        details.Age=request.POST['Age']
        details.Primary_fur_color=request.POST['Primary_fur_color']
        details.Location=request.POST['Location']
        details.Specific_location=request.POST['Specific_location']
        details.Running=request.POST['Running']
        details.Chaseing=request.POST['Chasing']
        details.Climbing=request.POST['Climbing']
        details.Eating=request.POST['Eating']
        details.Foraging=request.POST['Foraging']
        details.Other_Activities=request.POST['Other_Activities']
        details.Kuks=request.POST['Kuks']
        details.Quaas=request.POST['Quaas']
        details.Moans=request.POST['Moans']
        details.Tail_flags=request.POST['Tail_flags']
        details.Tail_twitches=request.POST['Tail_twitches']
        details.Approaches=request.POST['Approaches']
        details.Indifferent=request.POST['Indifferent']
        details.Runs_from=request.POST['Runs_from']
#	details.save()        
        

    context={'details':details}
    return render(request,'vwsquirrel/detail.html',context)
def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings')
    else:
        form = SightingForm()
    return render(request, 'squirrel_tracker/add.html', {'form': form})
