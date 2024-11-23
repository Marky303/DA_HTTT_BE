from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    path('overviewstats/'               , views.getOverviewStats),    
    path('overviewprogression/'         , views.getOverviewProgression),         
    path('topproducts/'                 , views.getTopProducts),
    path('topterritory/'                , views.getTopTerritory),
]