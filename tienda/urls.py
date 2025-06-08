from django.urls import path
from . import api_views, views

urlpatterns = [ 
    path("", views.index, name="index"),    

]