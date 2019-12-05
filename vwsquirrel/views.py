from django.shortcuts import render,get_object_or_404,redirect
from django.apps import apps
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import sq_model
from django.forms import ModelForm
from django.db.models import Count, Q
from .forms import SquForm
def index(request):
    squirrels = sq_model.objects.all()
    context = {'squirrels': squirrels,
            }
    return render(request, 'vwsquirrel/index.html', context)



def add(request):
    if request.method == 'POST':
        form = SquForm(request.POST)
        form.save()
        return redirect('/sightings/')
    return render(request,'vwsquirrel/add.html')

def map(request):
    squirrels=sq_model.objects.all()[:100]
    return render(request, 'vwsquirrel/map.html', {'squirrels':squirrels})

def detail(request,Unique_Squirrel_ID):
    details = sq_model.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
   # details = get_object_or_404(squ_model,Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        if 'delete' in request.POST:
            details.delete()
        else:
            x=list(request.POST.values())[1:]
            sqs = sq_model.objects.filter(Unique_Squirrel_ID=Unique_Squirrel_ID)
            details = SquForm(request.POST,instance=sqs[0])
            if details.is_valid():
                model=apps.get_model('vwsquirrel','sq_model')
                field_names = [f.name for f in model._meta.fields][1:]
                for sq in sqs:
                    for idx,f in enumerate(field_names):
                        if x[idx]:
                            setattr(sq,f,x[idx])
                    sq.save()
        return redirect('/sightings/')
    return render(request, 'vwsquirrel/detail.html',{'details':details})

def stats(request):
    Adult=sq_model.objects.filter(Age='Adult').count()
    Juvenile=sq_model.objects.filter(Age='Juvenile').count()
    AM=sq_model.objects.filter(Shift='AM').count()
    PM=sq_model.objects.filter(Shift='PM').count()
    Running=sq_model.objects.filter(Running=True).count()
    Chasing=sq_model.objects.filter(Chasing=True).count()
    Climbing=sq_model.objects.filter(Climbing=True).count()
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

