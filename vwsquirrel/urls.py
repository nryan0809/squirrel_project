from django.urls import path
from . import views
app_name = 'vwsquirrel'
urlpatterns = [
        path('', views.index, name='index'),
        path('<Unique_Squirrel_ID>/', views.details, name = "details"),
        ]
