from django.shortcuts import render,get_object_or_404,redirect
from django.apps import apps
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import squ_model
from django.forms import ModelForm
from django.db.models import Count, Q

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

def map(request):
    squirrels=squ_model.objects.all()[:100]
    return render(request, 'vwsquirrel/map.html', {'squirrels':squirrels})

def detail(request,Unique_Squirrel_ID):
    details = squ_model.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
   # details = get_object_or_404(squ_model,Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        if 'delete' in request.POST:
            details.delete()
        else:
            details = SquForm(instance=details,data=request.POST)
            if details.is_valid():
                 details.save()
        return redirect('/sightings/')
    return render(request, 'vwsquirrel/detail.html',{'details':details})

def stats(request):
    Adult=squ_model.objects.filter(Age='Adult').count()
    Juvenile=squ_model.objects.filter(Age='Juvenile').count()
    AM=squ_model.objects.filter(Shift='AM').count()
    PM=squ_model.objects.filter(Shift='PM').count()
    Running=squ_model.objects.filter(Running=True).count()
    Chasing=squ_model.objects.filter(Chasing=True).count()
    Climbing=squ_model.objects.filter(Climbing=True).count()
    context={
            'Adult':Adult,
            'Juvenile':Juvenile,
            'AM':AM,
            'PM':PM,
            'Running':Running,
            'Chasing':Chasing,
            'Climbing':Climbing,
            }
    return render(request,'vwsquirrel/stats.html',context)

