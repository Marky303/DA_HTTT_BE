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
    
    # Territory related
    path('getallterritory/'             , views.GetTerritory),
    
    # Product related
    path('getproductinformation/'       , views.GetProductInformation),
    path('createnewproduct/'            , views.CreateNewProduct),
    path('editproductinformation/'      , views.EditProductInformation),
    path('deleteproduct/'               , views.DeleteProduct),
    
    # Customer store related
    path('getcustomerstoreinformation'  , views.GetCustomerStoreInformation),
    path('createcustomerstore'          , views.CreateNewCustomerStore),
    path('editcustomerstoreinformation' , views.EditCustomerStoreInformation),
    path('deletecustomerstore'          , views.DeleteCustomerStore),
    
    # Customer individual related
    path('getcustomerindividualinformation'  , views.GetCustomerIndividualInformation),
    path('createcustomerindividual'          , views.CreateNewCustomerIndividual),
    path('editcustomerindividualinformation' , views.EditCustomerIndividualInformation),
    path('deletecustomerindividual'          , views.DeleteCustomerIndividual),
]