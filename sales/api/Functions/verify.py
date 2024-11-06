import os 
import ast
from dotenv import load_dotenv
from datetime import datetime

# Import models
from sales.models import *

dateTimeFormat = '%Y-%m-%d %H:%M:%S.%f'

# Special offer related________________________________________________________________
# Check if special offer exists
def VerifySpecialOfferExist(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer id
    specialOfferID = specialOfferInfo['specialOfferID']
    
    # Check if id exist
    exists = SpecialOffer.objects.filter(id=specialOfferID).exists()

    return exists



# Check if special offer info is valid
def VerifySpecialOfferInformation(request, error):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
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



# Product related______________________________________________________________________
# Check if product exists
def VerifyProductExist(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get special offer id
    productID = productInfo['productID']
    
    # Check if id exist
    exists = Product.objects.filter(id=productID).exists()

    return exists



# Check if product info is valid
def VerifyProductInformation(request, error):
    load_dotenv()
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Verify steps...
    
        

# Special offer - product related______________________________________________________
# Check if special offer product exists
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
    
    
    
# Sales order related__________________________________________________________________
def VerifySalesOrderExist(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrder = ast.literal_eval(dict)
    
    # Get salesorderheader id from dict
    salesOrderHeaderID   = salesOrder['salesOrderHeaderID']
    
    # Check if sales order exist
    exists = SalesOrderHeader.objects.filter(id=salesOrderHeaderID).exists()
    
    return exists



# Customer related_____________________________________________________________________
def VerifyCustomerExist(request):    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customer = ast.literal_eval(dict)
    
    # Get special offer id
    CustomerID = customer['CustomerID']
    
    # Check if id exist
    exists = Customer.objects.filter(id=CustomerID).exists()

    return exists
