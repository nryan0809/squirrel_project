from django.core.management.base import BaseCommand, CommandError
from vwsquirrel.models import squirrel_model as sm
import pandas as pd
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)    
    def handle(self, *args, **options):
        filepath=options['csv_file']
        datadf=pd.read_csv(filepath, usecols=['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
        field_name=['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']
        for index,row in datadf.iterrows():          
            try:
                obj=sm()
                for i,field in enumerate(row):
                    setattr(obj,field_name[i],field)
                obj.save()
            except :
                raise CommandError("don't exist")
