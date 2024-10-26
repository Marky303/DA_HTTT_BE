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
    path('createnewproduct/'            , views.CreateProduct),
    path('editproductinformation/'      , views.EditProductInformation),
    path('deleteproduct/'               , views.DeleteProduct),
    
    # Salesorder related
    path('createsalesorder/'            , views.CreateSalesOrder),
    path('deletesalesorder/'            , views.DeleteSalesOrder),
    path('editsalesorder/'              , views.EditSalesOrder),
    path('getsalesorderinformation/'    , views.GetAllSalesOrder),
    
    # Customer store related

]