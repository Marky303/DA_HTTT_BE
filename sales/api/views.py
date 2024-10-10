from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import serializers
from .serializers import *

# Import functions
from .Functions.verify import *
from .Functions.response import *
from .Functions.CRUD import *
from account.api.Functions.verify import *
from account.api.Functions.response import *
from account.api.Functions.CRUD import *

# Get Special Offer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSpecialOffer(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get special offer list
        specialOfferList = GetAllSpecialOffer()
        
        # Create serializer
        serializer = SpecialOfferSerializer(specialOfferList, many=True)  
        
        # Response
        return Response(serializer.data)
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



# Edit Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditSpecialOffer(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        VerifySpecialOfferExist(request, error)
        
        # Check if special offer info is valid
        VerifySpecialOfferInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        SaveNewSpecialOfferInformation(request)        
        
        # Response
        return ResponseSuccessful("Information edited successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



# Create new Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSpecialOffer(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer info is valid
        VerifySpecialOfferInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        CreateNewSpecialOffer(request)        
        
        # Response
        return ResponseSuccessful("Created new special offer")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Delete Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteSpecialOffer(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        VerifySpecialOfferExist(request, error)

        # Check if there is an error
        if error:
            raise Exception()
        
        # Delete special offer
        DeleteSpecialOfferWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted special offer")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Create new special offer product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSpecialOfferProduct(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer product already existed for adding
        if VerifySpecialOfferProductExist(request):
            raise Exception("SepcialOffer - Product already existed!")
        
        # Check if special offer exists
        VerifySpecialOfferExist(request, error)
        
        # Check if product exists
        VerifyProductExist(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Create new special offer - product
        CreateNewSpecialOfferProduct(request)        
        
        # Response
        return ResponseSuccessful("Created new special offer - product")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Create new special offer product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteSpecialOfferProduct(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer product doesnt exist for deleting
        if not VerifySpecialOfferProductExist(request):
            raise Exception("SepcialOffer - Product does not exist!")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        DeleteSpecialOfferProductWithID(request)        
        
        # Response
        return ResponseSuccessful("Deleted special offer - product")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 