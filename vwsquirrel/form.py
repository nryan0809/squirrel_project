from django.forms import ModelForm
from .models import squ_model
class SquForm(ModelForm):
    class Meta:
        model=squ_model
        fields=['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']

