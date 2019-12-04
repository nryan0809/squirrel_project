from django.urls import path
from . import views
app_name = 'vwsquirrel'
urlpatterns = [
       # path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('add/',views.add,name='add'),
        path('map/', views.map, name='map'),
        path('stats/',views.stats,name='stats'),
        path('<Unique_Squirrel_ID>/', views.detail, name = "detail"),
        
        ]
