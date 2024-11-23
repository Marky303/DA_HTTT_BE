from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json

# Import serializers
from .serializers import *

# Import functions
from account.api.Functions.verify import *

# Import sale functions
from dashboard.api.Functions.verify import *    # DROP THIS SHIT
from dashboard.api.Functions.CRUD import *
from dashboard.api.Functions.response import *
from dashboard.api.serializers import *

# Get dashboard contents
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOverviewStats(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Handle user prompt in request
        result = getOverviewThisMonthCRUD()
        
        # Serialize response
        serializedResult = SerializeResponse(result)
        
        # Response
        return ResponseObject(serializedResult)
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOverviewProgression(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Handle user prompt in request
        result = getOverviewLastMonthsCRUD()
        
        # Serialize response
        serializedResult = SerializeResponse(result)
        
        # Response
        return ResponseObject(serializedResult)
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTopProducts(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Handle user prompt in request
        result = getTopProductsCRUD()
        
        # Serialize response
        serializedResult = SerializeResponse(result)
        
        # Response
        return ResponseObject(serializedResult)
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTopTerritory(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Handle user prompt in request
        result = getTopTerritoryCRUD()
        
        # Serialize response
        serializedResult = SerializeResponse(result)
        
        # Response
        return ResponseObject(serializedResult)
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)