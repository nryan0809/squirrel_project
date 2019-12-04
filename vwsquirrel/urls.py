from django.urls import path
from . import views
app_name = 'vwsquirrel'
urlpatterns = [
        path('', views.index, name='index'),
        path('add/',views.add,name='add'),
        path('stats/',views.stats,name='stats'),
        path('<Unique_Squirrel_ID>/', views.detail, name = "detail"),
       # path('stats/',views.stats,name='stats'),
        ]
