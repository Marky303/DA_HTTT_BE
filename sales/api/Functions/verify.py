import os 
import ast
from dotenv import load_dotenv

def VerifySpecialOfferInformation(request):
    load_dotenv()
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Check if there is any error in user information
    error = []

    #.1 Check description word count
    
    
    #.2 Check type word count
    
    
    #.3 Check MinQty < MaxQty
    if not int(specialOfferInfo['MinQty']) < int(specialOfferInfo['MaxQty']):
        error.append("MinQty must be less than MaxQty")
    
    #.4 Check StartDate and EndDate
    
    
    #.5 Check DiscountPct
    if not 0 <= float(specialOfferInfo['DiscountPct']) <= 1:
        error.append("DiscountPct must be between 0 and 1")    
    
    return error