from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Prompt AI url
    path('prompt/'         , views.HandlePrompt),            
    
]