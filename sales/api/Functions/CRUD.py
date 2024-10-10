import ast

# Import models
from sales.models import *

def GetAllSpecialOffer():
    return SpecialOffer.objects.all()

def SaveNewSpecialOfferInformation(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer info from dict
    specialOfferID          = specialOfferInfo['specialOfferID']
    Description             = specialOfferInfo['Description']
    DiscountPct             = specialOfferInfo['DiscountPct']
    Type                    = specialOfferInfo['Type']
    StartDate               = specialOfferInfo['StartDate']
    EndDate                 = specialOfferInfo['EndDate']
    MinQty                  = specialOfferInfo['MinQty']
    MaxQty                  = specialOfferInfo['MaxQty']

    # Get special offer object
    specialOffer = SpecialOffer.objects.get(id=specialOfferID)
    
    # Edit info
    specialOffer.Description    = Description
    specialOffer.DiscountPct    = DiscountPct
    specialOffer.Type           = Type
    specialOffer.StartDate      = StartDate
    specialOffer.EndDate        = EndDate
    specialOffer.MinQty         = MinQty
    specialOffer.MaxQty         = MaxQty
    
    # Save info
    specialOffer.save()
    
def CreateNewSpecialOffer(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer info from dict
    Description             = specialOfferInfo['Description']
    DiscountPct             = specialOfferInfo['DiscountPct']
    Type                    = specialOfferInfo['Type']
    StartDate               = specialOfferInfo['StartDate']
    EndDate                 = specialOfferInfo['EndDate']
    MinQty                  = specialOfferInfo['MinQty']
    MaxQty                  = specialOfferInfo['MaxQty']
    
    # Create new special offer object
    specialOffer = SpecialOffer(Description=Description, 
                                DiscountPct=DiscountPct, 
                                Type=Type,
                                StartDate=StartDate,
                                EndDate=EndDate,
                                MinQty=MinQty,
                                MaxQty=MaxQty)
    
    # Save new special offer object
    specialOffer.save()

def DeleteSpecialOfferWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer id from dict
    specialOfferID   = specialOfferInfo['specialOfferID']
    
    # Get special offer object
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    
    # Delete special offer object
    specialOffer.delete()
    
def CreateNewSpecialOfferProduct(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Get ids from dict
    specialOfferID   = info['specialOfferID']
    productID        = info['productID']
    
    # Get special offer and product objects
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    product          = Product.objects.get(id=productID)
    
    # Create new special offer product object
    newObject = SpecialOfferProduct(SpecialOffer=specialOffer, Product=product)
    
    # Save new object
    newObject.save()
    
def DeleteSpecialOfferProductWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Get ids from dict
    specialOfferID   = info['specialOfferID']
    productID        = info['productID']
    
    # Get special offer and product objects
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    product          = Product.objects.get(id=productID)
    
    # Create new special offer product object
    deleteObject = SpecialOfferProduct.objects.get(SpecialOffer=specialOffer, Product=product)
    
    # Save new object
    deleteObject.delete()