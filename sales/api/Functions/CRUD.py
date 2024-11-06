import ast
from datetime import datetime
import random
import string
from decimal import Decimal
import math

# Import ETL functions
from analysis.api.Functions.CRUD import *

# Import models
from sales.models import *

# Get page index function
DEFAULT_PAGE_SIZE = 10

def getPageIndex(pageNumber, pageSize):
    startIndex = (pageNumber - 1) * pageSize
    endIndex   = startIndex + pageSize
    return (startIndex, endIndex)


# Special offer related_______________________________________________________________
# Get special offer list
def GetAllSpecialOfferCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get the page number
    page = specialOfferInfo["page"]
    pageIndexTuple = getPageIndex(page, DEFAULT_PAGE_SIZE)

    # Get the list
    lst = sorted(SpecialOffer.objects.all(), key=lambda obj: obj.id, reverse=True)

    # Get the total number of pages
    total_pages = math.ceil(len(lst) / DEFAULT_PAGE_SIZE)

    responseDict = {
        "content": lst[pageIndexTuple[0]:pageIndexTuple[1]],
        "totalPage": total_pages
    }

    return responseDict



# Save edited special offer info
def EditSpecialOfferCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer info from dict
    specialOfferID          = specialOfferInfo['specialOfferID']
    Description             = specialOfferInfo['Description']
    DiscountPct             = specialOfferInfo['DiscountPct']
    Type                    = specialOfferInfo['Type']
    StartDate               = specialOfferInfo['StartDate']
    EndDate                 = specialOfferInfo['EndDate']
    MinQty                  = specialOfferInfo['MinQty']
    MaxQty                  = specialOfferInfo['MaxQty']

    # Get special offer object
    specialOffer = SpecialOffer.objects.get(id=specialOfferID)
    
    # Edit info
    specialOffer.Description    = Description
    specialOffer.DiscountPct    = DiscountPct
    specialOffer.Type           = Type
    specialOffer.StartDate      = StartDate
    specialOffer.EndDate        = EndDate
    specialOffer.MinQty         = MinQty
    specialOffer.MaxQty         = MaxQty
    
    # Save info
    specialOffer.save()
    
    # ETL
    
    
    
    
# Create new special offer
def CreateSpecialOfferCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer info from dict
    Description             = specialOfferInfo['Description']
    DiscountPct             = specialOfferInfo['DiscountPct']
    Type                    = specialOfferInfo['Type']
    StartDate               = specialOfferInfo['StartDate']
    EndDate                 = specialOfferInfo['EndDate']
    MinQty                  = specialOfferInfo['MinQty']
    MaxQty                  = specialOfferInfo['MaxQty']
    
    # Create new special offer object
    specialOffer = SpecialOffer(Description=Description, 
                                DiscountPct=DiscountPct, 
                                Type=Type,
                                StartDate=StartDate,
                                EndDate=EndDate,
                                MinQty=MinQty,
                                MaxQty=MaxQty)
    
    # Save new special offer object
    specialOffer.save()
    
    # ETL
    CreateSpecialOfferDimETL(specialOffer)


# Delete special offer with ID from request
def DeleteSpecialOfferCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    specialOfferInfo = ast.literal_eval(dict)
    
    # Get special offer id from dict
    specialOfferID   = specialOfferInfo['specialOfferID']
    
    # Get special offer object
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    
    # Delete special offer object
    specialOffer.delete()
    
    
    
# Special offer - product related_____________________________________________________
# Create new special offer - product relation
def CreateSpecialOfferProductCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Get ids from dict
    specialOfferID   = info['specialOfferID']
    productID        = info['productID']
    
    # Get special offer and product objects
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    product          = Product.objects.get(id=productID)
    
    # Create new special offer product object
    newObject = SpecialOfferProduct(SpecialOffer=specialOffer, Product=product)
    
    # Save new object
    newObject.save()
    
    
    
# Delete special offer product relation
def DeleteSpecialOfferProductCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Get ids from dict
    specialOfferID   = info['specialOfferID']
    productID        = info['productID']
    
    # Get special offer and product objects
    specialOffer     = SpecialOffer.objects.get(id=specialOfferID)
    product          = Product.objects.get(id=productID)
    
    # Create new special offer product object
    deleteObject = SpecialOfferProduct.objects.get(SpecialOffer=specialOffer, Product=product)
    
    # Save new object
    deleteObject.delete()
    
    

# Get special offer - product relation list
def GetSpecialOfferProductCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Get product
    product = Product.objects.get(id=info['productID'])
    
    return SpecialOfferProduct.objects.filter(Product=product)



# Territory related___________________________________________________________________
# Get territory list
def GetTerritoryCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    territoryInfo = ast.literal_eval(dict)
    
    # Get the page number
    page = territoryInfo["page"]
    pageIndexTuple = getPageIndex(page, DEFAULT_PAGE_SIZE)

    # Get the list
    lst = sorted(Territory.objects.all(), key=lambda obj: obj.id, reverse=True)

    # Get the total number of pages
    total_pages = math.ceil(len(lst) / DEFAULT_PAGE_SIZE)

    responseDict = {
        "content": lst[pageIndexTuple[0]:pageIndexTuple[1]],
        "totalPage": total_pages
    }

    return responseDict



# Product related_____________________________________________________________________
# Get product list
def GetAllProduct(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get the page number
    page = productInfo["page"]
    pageIndexTuple = getPageIndex(page, DEFAULT_PAGE_SIZE)

    # Get the list
    lst = sorted(Product.objects.all(), key=lambda obj: obj.id, reverse=True)

    # Get the total number of pages
    total_pages = math.ceil(len(lst) / DEFAULT_PAGE_SIZE)

    responseDict = {
        "content": lst[pageIndexTuple[0]:pageIndexTuple[1]],
        "totalPage": total_pages
    }

    return responseDict



# Save edited product info
def EditProductCRUD(request):
    # Converting request.body to dictionary type
    dict        = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Extract new information from request
    productID           = productInfo['productID']
    Name                = productInfo['Name']
    Manufacturer        = productInfo['Manufacturer']
    Summary             = productInfo['Summary']
    WarrantyPeriod      = productInfo['WarrantyPeriod']
    RiderExperience     = productInfo['RiderExperience']
    Description         = productInfo['Description']
    ListPrice           = productInfo['ListPrice']
    StandardCost        = productInfo['StandardCost']
    Size                = productInfo['Size']
    Style               = productInfo['Style']
    
    # Get product
    product = Product.objects.get(id=productID)
    
    
    # Change new employee infomation
    product.Name                = Name
    product.Manufacturer        = Manufacturer
    product.Summary             = Summary
    product.WarrantyPeriod      = WarrantyPeriod
    product.RiderExperience     = RiderExperience
    product.Description         = Description
    product.ListPrice           = ListPrice
    product.StandardCost        = StandardCost
    product.Size                = Size
    product.Style               = Style
    
    # Save employee information
    product.save()
    
    
    
# Create new product
def CreateProductCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get product info from dict
    Name                = productInfo['Name']
    Manufacturer        = productInfo['Manufacturer']
    Summary             = productInfo['Summary']
    WarrantyPeriod      = productInfo['WarrantyPeriod']
    RiderExperience     = productInfo['RiderExperience']
    Description         = productInfo['Description']
    ListPrice           = productInfo['ListPrice']
    StandardCost        = productInfo['StandardCost']
    Size                = productInfo['Size']
    Style               = productInfo['Style']
    
    # Create new product object
    product = Product(Name=Name, Manufacturer=Manufacturer, Summary=Summary, WarrantyPeriod=WarrantyPeriod, RiderExperience=RiderExperience, Description=Description, ListPrice=ListPrice, StandardCost=StandardCost, Size=Size, Style=Style)
    
    # Save new product object
    product.save()



# Delete product with ID from database
def DeleteProductCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get product id from dict
    ProductID   = productInfo['productID']
    
    # Get product object
    product     = Product.objects.get(id=ProductID)
    
    # Delete product object
    product.delete()



# Sales order related_________________________________________________________________
# Generate random carrier tracking number func
def CreateCarrierTrackingNumber():
    X = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
    Y = ''.join(random.choice(string.digits) for _ in range(2))
    Z = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    return f"{X}-{Y}-{Z}"



# Create sales order details
def CreateSalesOrderDetailCRUD(request, headerID):
    # Get Sales order header object
    salesOrderHeader = SalesOrderHeader.objects.get(id=headerID)
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrderInfo      = ast.literal_eval(dict)
    salesOrderDetails   = salesOrderInfo["SalesOrderDetails"]
    
    # Calculate subTotal for SalesOrderHeader 
    subTotal = Decimal(0)
    
    salesOrderDetailList = []
    
    for salesOrderDetail in salesOrderDetails:
        # 0.Get SalesOrderDetail infos
        productID       = salesOrderDetail['productID']
        OrderQty        = salesOrderDetail['OrderQty']
        
        # 1.Get product object
        product         = Product.objects.get(id=productID)
        
        # 2.Automatically apply special offer
        # Get special offer - products
        specialOfferProducts        = SpecialOfferProduct.objects.filter(Product=product)
        
        # Filter special offers
        highestDiscount = Decimal(0)
        bestSpecialOffer = None
        for specialOfferProduct in specialOfferProducts:            
            # Get special offer
            specialOffer = specialOfferProduct.SpecialOffer 
            
            # Check if current date is valid
            currentDate = datetime.now()
            if specialOffer.EndDate:
                if not specialOffer.StartDate.replace(tzinfo=None) <= currentDate <= specialOffer.EndDate.replace(tzinfo=None):
                    continue
            else:
                if not specialOffer.StartDate.replace(tzinfo=None) <= currentDate:
                    continue 
            
            # Check if quantity is valid
            if specialOffer.MaxQty:
                if not specialOffer.MinQty <= int(OrderQty) <= specialOffer.MaxQty:
                    continue
            else:
                if not specialOffer.MinQty <= int(OrderQty):
                    continue
            
            print("Check")
            
            # Check highest rate
            if highestDiscount < specialOffer.DiscountPct:
                highestDiscount = specialOffer.DiscountPct
                bestSpecialOffer = specialOffer
           
        # 3.Calculate LineTotal
        LineTotal = Decimal(OrderQty) * product.ListPrice * (1 - highestDiscount)
                
        # 4.Generate carrier tracking number
        CarrierTrackingNumber = CreateCarrierTrackingNumber()
                
        # 5.Create SalesHeaderDetail
        salesOrderDetail = SalesOrderDetail(CarrierTrackingNumber=CarrierTrackingNumber,
                                            OrderQty=OrderQty,
                                            UnitPrice=product.ListPrice,
                                            UnitPriceDiscount=highestDiscount,
                                            LineTotal=LineTotal,
                                            SpecialOffer=bestSpecialOffer,
                                            Product=product,
                                            SalesOrder=salesOrderHeader)
        
        # 6.Append to list
        salesOrderDetailList.append(salesOrderDetail)
        
        # 7.Add to SubTotal 
        subTotal += LineTotal
        
    # SAVE IF THERE IS NO ERROR
    for item in salesOrderDetailList:
        item.save()
                
    # Update subTotal and other numbers of sales order
    salesOrderHeader.SubTotal = subTotal
    salesOrderHeader.TotalDue = subTotal + salesOrderHeader.Freight + salesOrderHeader.TaxAmt
    salesOrderHeader.save()
    
    return True
                    
        

# Create sales order header
def CreateSalesOrderHeaderCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrderInfo = ast.literal_eval(dict)

    # Get Sales order info from dict
    OrderDate   = salesOrderInfo['OrderDate']
    DueDate     = salesOrderInfo['DueDate']
    ShipDate    = salesOrderInfo['ShipDate']
    ShipMethod  = salesOrderInfo['ShipMethod']
    TaxAmt      = salesOrderInfo['TaxAmt']
    Freight     = salesOrderInfo['Freight']
    Comment     = salesOrderInfo['Comment']
    territory   = Territory.objects.get(id=salesOrderInfo['territoryID'])
    customer    = Customer.objects.get(id=salesOrderInfo['customerID'])
    user        = request.user    
    
    # Create new sales order header object
    salesOrderHeader = SalesOrderHeader(OrderDate=OrderDate,
                                        DueDate=DueDate,
                                        ShipDate=ShipDate,
                                        ShipMethod=ShipMethod,
                                        TaxAmt=TaxAmt,
                                        Freight=Freight,
                                        Comment=Comment,
                                        Employee=user,
                                        Territory=territory,
                                        Customer=customer)
    
    # Save object to database
    salesOrderHeader.save()
    
    # Return id for further processing
    return salesOrderHeader.id
    
    

# Edit sales order  
def EditSalesOrderHeaderCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrderInfo = ast.literal_eval(dict)

    # Get Sales order info from dict
    salesOrderID    = salesOrderInfo['id']
    OrderDate       = salesOrderInfo['OrderDate']
    DueDate         = salesOrderInfo['DueDate']
    ShipDate        = salesOrderInfo['ShipDate']
    ShipMethod      = salesOrderInfo['ShipMethod']
    TaxAmt          = salesOrderInfo['TaxAmt']
    Freight         = salesOrderInfo['Freight']
    Comment         = salesOrderInfo['Comment']
    territory       = Territory.objects.get(id=salesOrderInfo['territoryID'])
    customer        = Customer.objects.get(id=salesOrderInfo['customerID'])
    user            = request.user    
    
    # Get sales order object
    salesOrder      = SalesOrderHeader.objects.get(id=salesOrderID)
    
    # Create new sales order header object
    salesOrder.OrderDate    = OrderDate
    salesOrder.DueDate      = DueDate
    salesOrder.ShipDate     = ShipDate
    salesOrder.ShipMethod   = ShipMethod
    salesOrder.TaxAmt       = TaxAmt
    salesOrder.Freight      = Freight
    salesOrder.Comment      = Comment
    salesOrder.Employee     = user
    salesOrder.Territory    = territory
    salesOrder.Customer     = customer
    
    # Save object to database
    salesOrder.save()
    
    # Return id for further processing
    return salesOrder.id



# Delete all sales order detail from a sales order header
def DeleteAllSalesOrderDetailCRUD(headerID):
    # Get sales order header object
    salesOrderHeader        = SalesOrderHeader.objects.get(id=headerID)
    
    # Get sales order detail list
    salesOrderDetailList    = SalesOrderDetail.objects.filter(SalesOrder=salesOrderHeader)
    
    # Delete the list
    for salesOrderDetail in salesOrderDetailList:
        salesOrderDetail.delete()
    

# Delete sales order
def DeleteSalesOrderWithRequestCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrder = ast.literal_eval(dict)
    
    # Get salesorderheader id from dict
    salesOrderHeaderID   = salesOrder['salesOrderHeaderID']
    
    # Get sales order object
    salesOrder            = SalesOrderHeader.objects.get(id=salesOrderHeaderID)
    
    # Delete sales order object
    salesOrder.delete()
    
    
def DeleteSalesOrderWithID(salesOrderHeaderID:int):
    # Get sales order object
    salesOrder            = SalesOrderHeader.objects.get(id=salesOrderHeaderID)
    
    # Delete sales order object
    salesOrder.delete()
    

def GetSalesOrderCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerInfo = ast.literal_eval(dict)
    
    # Get the page number
    page = customerInfo["page"]
    pageIndexTuple = getPageIndex(page, DEFAULT_PAGE_SIZE)

    # Get the list
    lst = sorted(SalesOrderHeader.objects.all(), key=lambda obj: obj.id, reverse=True)

    # Get the total number of pages
    total_pages = math.ceil(len(lst) / DEFAULT_PAGE_SIZE)

    responseDict = {
        "content": lst[pageIndexTuple[0]:pageIndexTuple[1]],
        "totalPage": total_pages
    }

    return responseDict
    
    

# Customer related____________________________________________________________________
def CreateCustomerCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Check if customer store is created
    if "CustomerStore" in info:
        customerStore = info["CustomerStore"]
    else:
        return None
        
    # Get customer store info from dict
    Name                    = customerStore['Name']
    BusinessType            = customerStore['BusinessType']
    Specialty               = customerStore['Specialty']
    AnnualSales             = customerStore['AnnualSales']
    AnnualRevenue           = customerStore['AnnualRevenue']
    YearOpened              = customerStore['YearOpened']
    SquareFeet              = customerStore['SquareFeet']
    NumberOfEmployees       = customerStore['NumberOfEmployees']
    City                    = customerStore['City']
    AddressLine1            = customerStore['AddressLine1']
    AddressLine2            = customerStore['AddressLine2']
    CountryRegionName       = customerStore['CountryRegionName']
    
    # Create new customer store object
    store = CustomerStore(Name=Name, BusinessType=BusinessType, Specialty=Specialty, AnnualSales=AnnualSales, AnnualRevenue=AnnualRevenue, YearOpened=YearOpened, SquareFeet=SquareFeet, NumberOfEmployees=NumberOfEmployees, City=City, AddressLine1=AddressLine1, AddressLine2=AddressLine2, CountryRegionName=CountryRegionName)
        
    # Save new customer store object
    store.save()
    
    # Return store ID
    return store.id



def CreateNewCustomerIndividual(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = ast.literal_eval(dict)
    
    # Check if customer store is created
    if "CustomerIndividual" in info:
        customerIndividual = info["CustomerIndividual"]
    else:
        return None
    
    # Get customer individual info from dict
    FirstName               = customerIndividual['FirstName']
    LastName                = customerIndividual['LastName']
    MiddleName              = customerIndividual['MiddleName']
    Title                   = customerIndividual['Title']
    EmailAddress            = customerIndividual['EmailAddress']
    PhoneNumber             = customerIndividual['PhoneNumber']
    City                    = customerIndividual['City']
    AddressLine1            = customerIndividual['AddressLine1']
    AddressLine2            = customerIndividual['AddressLine2']
    CountryRegionName       = customerIndividual['CountryRegionName']
    
    # Create new customer individual object
    individual = CustomerIndividual(FirstName=FirstName, LastName=LastName, MiddleName=MiddleName, Title=Title, EmailAddress=EmailAddress, PhoneNumber=PhoneNumber, City=City, AddressLine1=AddressLine1, AddressLine2=AddressLine2, CountryRegionName=CountryRegionName)
        
    # Save new customer individual object
    individual.save()
    
    # Return customer individual ID
    return individual.id
    


def CreateNewCustomer(request, storeID, individualID):
    # Get customer store and customer individual
    if storeID:
        customerStore = CustomerStore.objects.get(id = storeID)
    else:
        customerStore = None
        
    if individualID:
        customerIndividual = CustomerIndividual.objects.get(id = individualID)
    else:
        customerIndividual = None
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerInfo = ast.literal_eval(dict)
    user = request.user
    territory = Territory.objects.get(id=customerInfo['territoryID'])
    
    # Create new Customer
    newCustomer = Customer(CustomerStore=customerStore, CustomerIndividual=customerIndividual,Employee=user, Territory=territory)

    # Save new customer
    newCustomer.save()
    


def EditCustomerCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerInfo = ast.literal_eval(dict)
    
    # Get customer id from request
    CustomerID = customerInfo["CustomerID"]
    customer = Customer.objects.get(id = CustomerID)
    
    # Customer store_________________________________
    # Get customer store object
    customerStore = customer.CustomerStore
    
    # Check if customerstore exist
    if "CustomerStore" in customerInfo:
        customerStoreInfo = customerInfo["CustomerStore"]
    else:
        customerStoreInfo = None
    
    if customerStoreInfo and customerStore:
        # Change new customer
        customerStore.Name                    = customerStoreInfo['Name']
        customerStore.BusinessType            = customerStoreInfo['BusinessType']
        customerStore.Specialty               = customerStoreInfo['Specialty']
        customerStore.AnnualSales             = customerStoreInfo['AnnualSales']
        customerStore.AnnualRevenue           = customerStoreInfo['AnnualRevenue']
        customerStore.YearOpened              = customerStoreInfo['YearOpened']
        customerStore.SquareFeet              = customerStoreInfo['SquareFeet']
        customerStore.NumberOfEmployees       = customerStoreInfo['NumberOfEmployees']
        customerStore.City                    = customerStoreInfo['City']
        customerStore.AddressLine1            = customerStoreInfo['AddressLine1']
        customerStore.AddressLine2            = customerStoreInfo['AddressLine2']
        customerStore.CountryRegionName       = customerStoreInfo['CountryRegionName']
        
        # Save new customer store
        customerStore.save()
        
    elif customerStoreInfo and (not customerStore):
        customerStore = CustomerStore(Name              =customerStoreInfo['Name'],
                                      BusinessType      =customerStoreInfo['BusinessType'],
                                      Specialty         =customerStoreInfo['Specialty'],
                                      AnnualSales       =customerStoreInfo['AnnualSales'],
                                      AnnualRevenue     =customerStoreInfo['AnnualRevenue'],
                                      YearOpened        =customerStoreInfo['YearOpened'],
                                      SquareFeet        =customerStoreInfo['SquareFeet'],
                                      NumberOfEmployees =customerStoreInfo['NumberOfEmployees'],
                                      City              =customerStoreInfo['City'],
                                      AddressLine1      =customerStoreInfo['AddressLine1'],
                                      AddressLine2      =customerStoreInfo['AddressLine2'],
                                      CountryRegionName =customerStoreInfo['CountryRegionName'])
        customerStore.save()
        customer.CustomerStore = customerStore

         
    elif (not customerStoreInfo) and customerStore:
        customerStore.delete()
        customer.CustomerStore = None
    
    # Customer individual____________________________
    # Get customer individual object
    customerIndividual = customer.CustomerIndividual
    
    # Check if customerindividual exist
    if "CustomerIndividual" in customerInfo:
        customerIndividualInfo = customerInfo["CustomerIndividual"]
    else:
        customerIndividualInfo = None
    
    if customerIndividualInfo and customerIndividual:
        # Change new customer individual
        customerIndividual.FirstName               = customerIndividualInfo['FirstName']
        customerIndividual.LastName                = customerIndividualInfo['LastName']
        customerIndividual.MiddleName              = customerIndividualInfo['MiddleName']
        customerIndividual.Title                   = customerIndividualInfo['Title']
        customerIndividual.EmailAddress            = customerIndividualInfo['EmailAddress']
        customerIndividual.PhoneNumber             = customerIndividualInfo['PhoneNumber']
        customerIndividual.City                    = customerIndividualInfo['City']
        customerIndividual.AddressLine1            = customerIndividualInfo['AddressLine1']
        customerIndividual.AddressLine2            = customerIndividualInfo['AddressLine2']
        customerIndividual.CountryRegionName       = customerIndividualInfo['CountryRegionName']
    
        # Save new customer individual
        customerIndividual.save()
    
    elif customerIndividualInfo and (not customerIndividual):    
        customerIndividual = CustomerIndividual(FirstName           =customerIndividualInfo['FirstName'],
                                                LastName            =customerIndividualInfo['LastName'],
                                                MiddleName          =customerIndividualInfo['MiddleName'],
                                                Title               =customerIndividualInfo['Title'],
                                                EmailAddress        =customerIndividualInfo['EmailAddress'],
                                                PhoneNumber         =customerIndividualInfo['PhoneNumber'],
                                                City                =customerIndividualInfo['City'],
                                                AddressLine1        =customerIndividualInfo['AddressLine1'],
                                                AddressLine2        =customerIndividualInfo['AddressLine2'],
                                                CountryRegionName   =customerIndividualInfo['CountryRegionName'])
        customerIndividual.save()
        customer.CustomerIndividual = customerIndividual
    
    elif (not customerIndividualInfo) and customerIndividual:
        customerIndividual.delete()
        customer.CustomerIndividual = None
    
    # Change new territory
    customer.Territory = Territory.objects.get(id=customerInfo['Territory'])
    
    # Save new customer to database
    customer.save()
    
    # Return id for further processing
    return customer.id



def DeleteCustomerCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerInfo = ast.literal_eval(dict)
    
    # Get customer id from dict
    CustomerID   = customerInfo['CustomerID']
    
    # Get customer object
    customer     = Customer.objects.get(id=CustomerID)
    
    # Delete customer store and customer individual if exist
    if customer.CustomerIndividual:
        customer.CustomerIndividual.delete()
    if customer.CustomerStore:
        customer.CustomerStore.delete()
    
    # Delete customer object
    customer.delete()
    


def GetCustomerCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerInfo = ast.literal_eval(dict)
    
    # Get the page number
    page = customerInfo["page"]
    pageIndexTuple = getPageIndex(page, DEFAULT_PAGE_SIZE)

    # Get the list
    lst = sorted(Customer.objects.all(), key=lambda obj: obj.id, reverse=True)

    # Get the total number of pages
    total_pages = math.ceil(len(lst) / DEFAULT_PAGE_SIZE)

    responseDict = {
        "content": lst[pageIndexTuple[0]:pageIndexTuple[1]],
        "totalPage": total_pages
    }

    return responseDict
