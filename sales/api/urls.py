from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    path('getallspecialoffers/', views.GetSpecialOffer),             # Get employee information endpoint
    path('editspecialoffer/', views.EditSpecialOffer),
    path('createspecialoffer/', views.CreateSpecialOffer),

    
]