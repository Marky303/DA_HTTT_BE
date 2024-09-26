from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    path('getemployeeinfo/', views.GetEmployeeInformation),             # Get employee information endpoint
    path('editemployeeinfo/', views.EditEmployeeInformation),           # Edit employee information endpoint
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Note example url
    path('getNotes/', views.getNotes)
    
]