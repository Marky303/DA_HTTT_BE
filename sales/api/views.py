from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import acount
from account.api.Functions.verify import *
from account.api.Functions.response import *
from account.api.Functions.CRUD import *

# Import sale
from sales.api.Functions.verify import *
from sales.api.Functions.CRUD import *
from sales.api.Functions.response import *
from sales.api.serializers import *


# Get employee information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetProductInformation(request):
    product = request.product
    serializer = ProductInfoSerializer(product)
    return Response(serializer.data)


# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditProductInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyProductExist(request):
            raise Exception("Don't have a product")
                
        # Verify if employee information is valid
        error = VerifyProductInformation(request)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If employee information is valid, save new employee information
        SaveNewProduct(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

# Create new Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProduct(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer info is valid
        VerifyProductInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        CreateNewProduct(request)        
        
        # Response
        return ResponseSuccessful("Created new product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
# Delete Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteProduct(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifyProductExist(request):
            raise Exception("Product does not exist")
        
        # Delete special offer
        DeleteProductWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 








# Get customer store information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCustomerStoreInformation(request):
    store = request.store
    serializer = CustomerStoreInfoSerializer(store)
    return Response(serializer.data)


# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditCustomerStoreInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyProductExist(request):
            raise Exception("Don't have a customer store")
                
        # Verify if employee information is valid
        error = VerifyCustomerStoreInformation(request)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If employee information is valid, save new employee information
        SaveNewCustomerStore(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

# Create new Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateCustomerStore(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer info is valid
        VerifyCustomerStoreInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        CreateNewCustomerStore(request)        
        
        # Response
        return ResponseSuccessful("Created new product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
# Delete Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteCustomerStore(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifyCustomerStoreExist(request):
            raise Exception("Product does not exist")
        
        # Delete special offer
        DeleteCustomerStoreWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)






# Get customer individual information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCustomerIndividualInformation(request):
    individual = request.individual
    serializer = CustomerIndividualInfoSerializer(individual)
    return Response(serializer.data)


# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditCustomerIndividualInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyProductExist(request):
            raise Exception("Don't have a customer individual")
                
        # Verify if employee information is valid
        error = VerifyCustomerIndividualInformation(request)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If employee information is valid, save new employee information
        SaveNewCustomerIndividual(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

# Create new Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateCustomerIndividual(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer info is valid
        VerifyCustomerIndividualInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer
        CreateNewCustomerIndividual(request)        
        
        # Response
        return ResponseSuccessful("Created new product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
# Delete Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteCustomerIndividual(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifyCustomerIndividualExist(request):
            raise Exception("Product does not exist")
        
        # Delete special offer
        DeleteCustomerIndividualWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
















# # EXAMPLE FOR TESTING
# from sales.models import *
# from .serializers import NoteSerializer

# # Example: get all notes of a certain user
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)



