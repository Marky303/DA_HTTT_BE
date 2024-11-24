from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import serializers
from .serializers import *

# Import functions
from .Functions.verify import *
from .Functions.response import *
from .Functions.CRUD import *


# Get employee information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetEmployeeInformation(request):
    user = request.user
    serializer = UserinfoSerializer(user)
    return Response(serializer.data)


# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditEmployeeInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
                
        # Verify if employee information is valid
        error = VerifyEmployeeInformation(request)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If employee information is valid, save new employee information
        SaveNewEmployeeInformation(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        
    except Exception as e:
        # Response a error code and error content        
        if str(e):
            print(str(e))
            error.append(str(e))
        print(error)
        return ResponseError(error)
    
        






















