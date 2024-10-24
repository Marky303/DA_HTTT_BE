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

# Import sale
from sales.api.Functions.verify import *
from sales.api.Functions.CRUD import *
from sales.api.Functions.response import *
from sales.api.serializers import *

# Get Special Offer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSpecialOffer(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
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
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifySpecialOfferExist(request):
            raise Exception("Special offer does not exist")
        
        # Check if special offer info is valid
        VerifySpecialOfferInformation(request, error)
        
        # Edit special offer
        SaveNewSpecialOfferInformation(request)        
        
        # Response
        return ResponseSuccessful("Information edited successfully")
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



# Get employee information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetProductInformation(request):
    product = Product.objects.all()
    serializer = ProductInfoSerializer(product, many=True)
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
        # error = VerifyProductInformation(request)
        
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
def CreateSpecialOffer(request):
    try:
        error = []
    
        # Check if special offer info is valid
        VerifySpecialOfferInformation(request, error)
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
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
    
    
def CreateProduct(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # VerifyProductInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
                
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
def DeleteSpecialOffer(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifySpecialOfferExist(request):
            raise Exception("Special offer does not exist")
        
        # Delete special offer
        DeleteSpecialOfferWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted special offer")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
def DeleteProduct(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if product exists
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
    
    
    
# Create new special offer product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSpecialOfferProduct(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if special offer exists
        if not VerifySpecialOfferExist(request):
            raise Exception("Special offer does not exist")
        
        # Check if product exists
        if not VerifyProductExist(request):
            raise Exception("Product does not exist")
        
        # Check if special offer product already existed for adding
        if VerifySpecialOfferProductExist(request):
            raise Exception("SepcialOffer - Product already existed!")
        
        # Create new special offer - product
        CreateNewSpecialOfferProduct(request)        
        
        # Response
        return ResponseSuccessful("Created new special offer - product")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Get all special offer product
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSpecialOfferProduct(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Get special offer list
        specialOfferProductList = GetAllSpecialOfferProduct()
        
        # Create serializer
        serializer = SpecialOfferProductSerializer(specialOfferProductList, many=True)  
        
        # Response
        return Response(serializer.data)
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))



# Get customer store information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCustomerStoreInformation(request):
    store = CustomerStore.objects.all()
    serializer = CustomerStoreInfoSerializer(store, many=True)
    return Response(serializer.data)



# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditCustomerStoreInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyCustomerStoreExist(request):
            raise Exception("Don't have a customer store")
                
        # Verify if employee information is valid
        # error = VerifyCustomerStoreInformation(request)
        
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
    
    
    
# Delete special offer product
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
        # VerifyCustomerStoreInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        CreateNewCustomerStore(request)        
        
        # Response
        return ResponseSuccessful("Created new customer store successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Get all territory view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetTerritory(request):
    territoryList = GetAllTerritory()
    serializer = TerritorySerializer(territoryList, many=True)  
    return Response(serializer.data)
    
    
    
# Delete Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteCustomerStore(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        
        # Check if customer store exists
        if not VerifyCustomerStoreExist(request):
            raise Exception("Customer store does not exist")
        
        # Delete special offer
        DeleteCustomerStoreWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted customer store successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)  



# Get customer individual information view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCustomerIndividualInformation(request):
    individual = CustomerIndividual.objects.all()
    serializer = CustomerIndividualInfoSerializer(individual, many=True)
    return Response(serializer.data)



# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditCustomerIndividualInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyCustomerIndividualExist(request):
            raise Exception("Don't have a customer individual")
                
        # Verify if employee information is valid
        # error = VerifyCustomerIndividualInformation(request)
        
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
        # VerifyCustomerIndividualInformation(request, error)
        
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
