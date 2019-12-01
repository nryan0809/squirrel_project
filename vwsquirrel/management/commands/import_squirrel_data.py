from django.core.management.base import BaseCommand, CommandError
from vwsquirrel.models import squirrel_model as sm
import pandas as pd
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass    
    def handle(self, *args, **options):
        filepath='file.csv'
        datadf=pd.read_csv(filepath, usecols=["x","y","unique_squirrel_id","shift","date","age","primary_fur_color","location","specific_location","running","chasing","climbing","eating","foraging","other_activities","kuks","quaas","moans","tail_flags","tail_twitches","approaches","indifferent","runs_from"])
        field_name=['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']
        for row in datadf:          
            try:
                obj=sm()
                for i,field in enumerate(row):
                    setattr(obj,fields_name[i],field)
                obj.save()
            except :
                raise CommandError("don't exist")
