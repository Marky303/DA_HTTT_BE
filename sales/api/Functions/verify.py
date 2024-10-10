import os 
import ast
from dotenv import load_dotenv
from datetime import datetime

# Import models
from sales.models import *

dateTimeFormat = '%Y-%m-%d %H:%M:%S.%f'

def VerifySpecialOfferExist(request, error):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer id
    specialOfferID = specialOfferInfo['specialOfferID']
    
    # Check if id exist
    exists = SpecialOffer.objects.filter(id=specialOfferID).exists()

    if not exists:
        error.append('Special offer does not exist!')



def VerifySpecialOfferInformation(request, error):
    load_dotenv()
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Check if there is any error in user information

    #.1 Check description word count
    
    
    #.2 Check type word count
    
    
    #.3 Check MinQty < MaxQty
    if not int(specialOfferInfo['MinQty']) < int(specialOfferInfo['MaxQty']):
        error.append("MinQty must be less than MaxQty")
    
    #.4 Check StartDate and EndDate
    startDate = datetime.strptime(specialOfferInfo['StartDate'], dateTimeFormat)
    endDate = datetime.strptime(specialOfferInfo['EndDate'], dateTimeFormat)
    if startDate >= endDate:
        error.append("Start date must be before end date")
    
    #.5 Check DiscountPct
    if not 0 <= float(specialOfferInfo['DiscountPct']) <= 1:
        error.append("DiscountPct must be between 0 and 1")    
        
    #.6 Check if overlapp other special offers
   
   
   
def VerifyProductExist(request, error):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get special offer id
    productID = productInfo['productID']
    
    # Check if id exist
    exists = Product.objects.filter(id=productID).exists()

    if not exists:
        error.append('Product does not exist!')
        


def VerifySpecialOfferProductExist(request):
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
    exists = SpecialOfferProduct.objects.filter(SpecialOffer=specialOffer, Product=product).exists()
    
    return exists