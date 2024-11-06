from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import serializers
from .serializers import *

# Import functions
from account.api.Functions.verify import *

# Import sale functions
from sales.api.Functions.verify import *
from sales.api.Functions.CRUD import *
from sales.api.Functions.response import *
from sales.api.serializers import *

# Special offer related__________________________________________________________
# Get Special Offer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetSpecialOffer(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get special offer list
        response = GetAllSpecialOffer(request)
        
        # Create serializer for special offer
        serializer = SpecialOfferSerializer(response["content"], many=True)  
        
        # Response
        return ResponseList(serializer.data, response["totalPage"])
          
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
    
        # Verify if user is an employee
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
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit special offer in database
        SaveNewSpecialOfferInformation(request)        
        
        # Response
        return ResponseSuccessful("Information edited successfully")
    
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



# Product related________________________________________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetProductInformation(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get special offer list
        response = GetAllProduct(request)
        
        # Create serializer for special offer
        serializer = ProductSerializer(response["content"], many=True)  
        
        # Response
        return ResponseList(serializer.data, response["totalPage"])
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



# Edit product information
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditProductInformation(request):
    try:
        error = []
        
        # Verify if user is an employee
        if not VerifyProductExist(request):
            raise Exception("Product does not exist")
                
        # Verify if product information is valid
        VerifyProductInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If product information is valid, save new product information
        SaveNewProduct(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        

    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Create new product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProduct(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        VerifyProductInformation(request, error)
        
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
    

    
# Delete product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteProduct(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if product exists
        if not VerifyProductExist(request):
            raise Exception("Product does not exist")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Delete product from database
        DeleteProductWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted product successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    


# Special offer - product related__________________________________________________
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
            raise Exception("Special offer already applied on this product")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Create new special offer - product
        CreateNewSpecialOfferProduct(request)        
        
        # Response
        return ResponseSuccessful("Added a new special offer for this product")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 
    
    
    
# Get all special offer product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetSpecialOfferProduct(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Get special offer list
        specialOfferProductList = GetAllSpecialOfferProduct(request)
        
        # Create serializer
        serializer = SpecialOfferProductSerializer(specialOfferProductList, many=True)  
        
        # Response
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
          
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
        return ResponseError(error)



# Territory related______________________________________________________________
# Get all territory view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetTerritory(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get special offer list
        response = GetAllTerritory(request)
        
        # Create serializer for special offer
        serializer = TerritorySerializer(response["content"], many=True)  
        
        # Response
        return ResponseList(serializer.data, response["totalPage"])
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error) 



# Sale order related_____________________________________________________________
# Create sales order
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSalesOrder(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Verify sales order information
        # TODO
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # CRUD
        headerID = None
        headerID = CreateNewSalesOrderHeader(request)
        CreateNewSalesOrderDetail(request, headerID)
        
        # Response
        return ResponseSuccessful("Created new salesorder")
          
    except Exception as e:
        # Revert created header
        if headerID:
            DeleteSalesOrderWithID(headerID)
        
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



# Edit sales order
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditSalesOrder(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Verify sales order information
        # TODO
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # CRUD
        headerID = SaveNewSalesOrderHeader(request)
        DeleteAllSalesOrderDetail(headerID)
        CreateNewSalesOrderDetail(request, headerID)
        
        # Response
        return ResponseSuccessful("Edited salesorder info")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



# Delete a salesorder
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteSalesOrder(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if sales order doesnt exist for deleting
        if not VerifySalesOrderExist(request):
            raise Exception("Sales order does not exist!")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit sales order
        DeleteSalesOrderWithIDreq(request)        
        
        # Response
        return ResponseSuccessful("Deleted sales order")
    
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    


# Get all salesorder
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetAllSalesOrder(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all sales order
        response =  GetSalesOrder(request)
        
        # Create serializer for special offer
        serializer = SalesOrderHeaderSerializer(response["content"], many=True)  
        
        # Response
        return ResponseList(serializer.data, response["totalPage"])
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



# Customer related_______________________________________________________________
# Get all customer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetCustomerInformation(request):
    try:
        error = []
    
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Get customer list
        response = GetAllCustomer(request)
        
        # Create serializer for special offer
        serializer = CustomerInfoSerializer(response["content"], many=True)  
        
        # Response
        return ResponseList(serializer.data, response["totalPage"])
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
    
# Create Customer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateCustomer(request):
    try:
        error = []
    
        # Verify if user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if customer info is valid
        # VerifyCustomerInformation(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Check if store or customer is available
        # Converting request.body to dictionary type
        dict = request.body.decode("UTF-8")
        info = ast.literal_eval(dict)
        
        if not ("CustomerStore" in info or "CustomerIndividual" in info):
            return ResponseError("Bruhhhh")
        
        # Edit customer
        storeID = CreateNewCustomerStore(request)
        individualID = CreateNewCustomerIndividual(request)
        CreateNewCustomer(request, storeID, individualID)    
        
        # Response
        return ResponseSuccessful("Created new customer successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
    
# Edit employee information view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditCustomerInformation(request):
    try:
        error = []
        
        # Verify is user is an employee
        if not VerifyCustomerExist(request):
            raise Exception("Don't have a customer")
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # If customer information is valid, save new customer information
        SaveNewCustomer(request)
        
        # Response successful code
        return ResponseSuccessful("Information edited successfully")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



# Delete Customer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteCustomer(request):
    try:     
        error = []
        
        # Verify is user is an employee
        if not VerifyEmployee(request):
            raise Exception("You are not an employee")
        
        # Check if customer exists
        if not VerifyCustomerExist(request):
            raise Exception("Customer does not exist")
        
        # Delete customer
        DeleteCustomerWithID(request)
        
        # Response
        return ResponseSuccessful("Deleted customer successfully")
          
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
