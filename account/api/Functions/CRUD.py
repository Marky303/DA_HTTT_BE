import ast

# Import models
from account.models import *

# ETL
from analysis.api.Functions.CRUD import *

def SaveNewEmployeeInformation(request):
    # Get user from request
    user = request.user
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    # dict = dict.replace("null", "None")
    userinfo = ast.literal_eval(dict)
    
    # Extract new information from request
    new_name = userinfo['name']
    new_JobTitle = userinfo['JobTitle']
    new_PhoneNumber = userinfo['PhoneNumber']
    new_City = userinfo['City']
    new_AddressLine1 = userinfo['AddressLine1']
    new_AddressLine2 = userinfo['AddressLine2']
    new_CountryRegionName = userinfo['CountryRegionName']
    
    # Change new employee infomation
    user.name = new_name
    user.JobTitle = new_JobTitle
    user.PhoneNumber = new_PhoneNumber
    user.City = new_City
    user.AddressLine1 = new_AddressLine1
    user.AddressLine2 = new_AddressLine2
    user.CountryRegionName = new_CountryRegionName
    
    # Save employee information
    user.save()
    
    # ETL
    EditEmployeeDimETL(user)
    