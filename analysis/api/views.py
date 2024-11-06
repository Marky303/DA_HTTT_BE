from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import serializers
from .serializers import *

# Import functions
from account.api.Functions.verify import *

# Import analysis functions
from analysis.api.Functions.verify import *
from analysis.api.Functions.CRUD import *
from analysis.api.Functions.response import *
from analysis.api.serializers import *

# Import gemini related
from analysis.gemini.GeminiController import *
from analysis.gemini.Functions.SerializeResponse import SerializeResponse

# Handle and process prompt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def HandlePrompt(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Handle user prompt in request
        result = GeminiController(request)
        
        # Serialize response
        serializedResult = SerializeResponse(result)
        
        # Response
        return ResponseObject(serializedResult)
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 