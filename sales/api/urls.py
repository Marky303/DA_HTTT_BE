from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Special offer related
    path('getspecialoffer/'             , views.GetSpecialOffer),            
    path('editspecialoffer/'            , views.EditSpecialOffer),
    path('createspecialoffer/'          , views.CreateSpecialOffer),
    path('deletespecialoffer/'          , views.DeleteSpecialOffer),

    # Special offer product related
    path('createspecialofferproduct/'   , views.CreateSpecialOfferProduct),
    path('deletespecialofferproduct/'   , views.DeleteSpecialOfferProduct),
    path('getallspecialofferproduct/'   , views.GetSpecialOfferProduct),
    
    # Territory related
    path('getterritory/'                , views.GetTerritory),
    
    # Product related
    path('getproduct/'                  , views.GetProductInformation),
    path('createproduct/'               , views.CreateProduct),
    path('editproduct/'                 , views.EditProductInformation),
    path('deleteproduct/'               , views.DeleteProduct),
    
    # Salesorder related
    path('createsalesorder/'            , views.CreateSalesOrder),
    path('deletesalesorder/'            , views.DeleteSalesOrder),
    path('editsalesorder/'              , views.EditSalesOrder),
    path('getsalesorder/'               , views.GetAllSalesOrder),
        
    # Customer related
    path('getcustomerinformation/'      , views.GetCustomerInformation),
    path('createcustomer/'              , views.CreateCustomer),
    path('editcustomerinformation/'     , views.EditCustomerInformation),
    path('deletecustomer/'              , views.DeleteCustomer),
]