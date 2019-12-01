from django.urls import path
<<<<<<< HEAD

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index')
    ]
=======
from . import views
app_name = 'vwsquirrel'
urlpatterns = [
        path('', views.index, name='index'),
        ]
>>>>>>> 8226e84c9c6fad8e31d65a22447fa3d6d936159e
