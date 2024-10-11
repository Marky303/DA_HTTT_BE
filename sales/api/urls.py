from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Special offer related
    path('getallspecialoffer/'         , views.GetSpecialOffer),            
    path('editspecialoffer/'            , views.EditSpecialOffer),
    path('createspecialoffer/'          , views.CreateSpecialOffer),
    path('deletespecialoffer/'          , views.DeleteSpecialOffer),

    # Special offer product related
    path('createspecialofferproduct/'   , views.CreateSpecialOfferProduct),
    path('deletespecialofferproduct/'   , views.DeleteSpecialOfferProduct),
    path('getallspecialofferproduct/'   , views.GetSpecialOfferProduct),
    
]