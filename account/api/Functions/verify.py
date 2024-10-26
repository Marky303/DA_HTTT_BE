import ast
import re

# Import models
from account.models import *

# Regular expressions
phone_number_pattern = r'^[\d\+\-\(\)\s]+$'


# Verify is user is actually an employee
def VerifyEmployee(request):
    user = request.user
    return user.isEmployee


# Verify if new user information is valid
def VerifyEmployeeInformation(request):    
    # Get user
    user = request.user
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    userinfo = ast.literal_eval(dict)
    
    # Check if there is any error in user information
    error = []
    
    #.1 Check if name is unique
    if not user.name == userinfo['name']:
        try:
            check_user = Employee.objects.get(name=userinfo['name'])
            error.append("Name has been taken")
        except:
            pass
    
    #.2 Check if any field is empty (DONT DO THIS)
    # if any(value in ('', None, []) for value in userinfo.values()):
    #     error.append("Fields must not be empty")

    #.3 Check if phone number is correct
    if not re.fullmatch(phone_number_pattern, userinfo['PhoneNumber']):
        error.append("Wrong phone number format")

    #.x Check if ...
    
    return error