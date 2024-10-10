from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    path('getallspecialoffers/', views.GetSpecialOffer),            
    path('editspecialoffer/', views.EditSpecialOffer),
    path('createspecialoffer/', views.CreateSpecialOffer),
    path('deletespecialoffer/', views.DeleteSpecialOffer),

    
]