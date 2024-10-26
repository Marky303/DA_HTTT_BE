import ast
from datetime import datetime
import random
import string
from decimal import Decimal

# Import models
from sales.models import *


# Special offer related_______________________________________________________________
# Get special offer list
def GetAllSpecialOffer():
    return SpecialOffer.objects.all()



# Save edited special offer info
def SaveNewSpecialOfferInformation(request):
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
    
    
    
# Create new special offer
def CreateNewSpecialOffer(request):
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



# Delete special offer with ID from request
def DeleteSpecialOfferWithID(request):
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
def CreateNewSpecialOfferProduct(request):
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
def DeleteSpecialOfferProductWithID(request):
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
def GetAllSpecialOfferProduct():
    return SpecialOfferProduct.objects.all()



# Territory related___________________________________________________________________
# Get territory list
def GetAllTerritory():
    return Territory.objects.all()



# Product related_____________________________________________________________________
# Get product list
def GetAllProduct():
    return Product.objects.all()



# Save edited product info
def SaveNewProduct(request):
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
    
    #Get product
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
def CreateNewProduct(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get special offer info from dict
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
    
    # Create new special offer object
    product = Product(Name=Name, Manufacturer=Manufacturer, Summary=Summary, WarrantyPeriod=WarrantyPeriod, RiderExperience=RiderExperience, Description=Description, ListPrice=ListPrice, StandardCost=StandardCost, Size=Size, Style=Style)
    
    # Save new special offer object
    product.save()



# Delete product with ID from database
def DeleteProductWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get special offer id from dict
    ProductID   = productInfo['productID']
    
    # Get special offer object
    product     = Product.objects.get(id=ProductID)
    
    # Delete special offer object
    product.delete()



# Sales order related_________________________________________________________________
# Generate random carrier tracking number func
def CreateCarrierTrackingNumber():
    X = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
    Y = ''.join(random.choice(string.digits) for _ in range(2))
    Z = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    return f"{X}-{Y}-{Z}"



# Create sales order details
def CreateNewSalesOrderDetail(request, headerID):
    # Get Sales order header object
    salesOrderHeader = SalesOrderHeader.objects.get(id=headerID)
    
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrderInfo      = ast.literal_eval(dict)
    salesOrderDetails   = salesOrderInfo["SalesOrderDetails"]
    
    # Calculate subTotal for SalesOrderHeader 
    subTotal = Decimal(0)
    
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
            if not specialOffer.StartDate.replace(tzinfo=None) <= currentDate <= specialOffer.EndDate.replace(tzinfo=None):
                continue
            
            # Check if quantity is valid
            if not specialOffer.MinQty <= OrderQty <= specialOffer.MaxQty:
                continue
            
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
        
        # 6.Save SalesHeaderDetail
        salesOrderDetail.save()
        
        # 7.Add to SubTotal 
        subTotal += LineTotal
                
    # Update subTotal and other numbers of sales order
    salesOrderHeader.SubTotal = subTotal
    salesOrderHeader.TotalDue = subTotal + salesOrderHeader.Freight + salesOrderHeader.TaxAmt
    salesOrderHeader.save()
                    
        

# Create sales order header
def CreateNewSalesOrderHeader(request):
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
def SaveNewSalesOrder(request):
    pass



# Delete sales order
def DeleteSalesOrderWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    salesOrder = ast.literal_eval(dict)
    
    # Get salesorderheader id from dict
    salesOrderHeaderID   = salesOrder['salesOrderHeaderID']
    
    # Get sales order object
    salesOrder            = SalesOrderHeader.objects.get(id=salesOrderHeaderID)
    
    # Delete sales order object
    salesOrder.delete()
    
    

# Customer related____________________________________________________________________
def GetAllCustomerStore():
    return CustomerStore.objects.all()

def SaveNewCustomerStore(request):
    # Converting request.body to dictionary type
    dict        = request.body.decode("UTF-8")
    customerStore = ast.literal_eval(dict)
    
    # Extract new information from request
    StoreID                 = customerStore['StoreID']
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
    
    #Get product
    store = CustomerStore.objects.get(id=StoreID)
    
    
    # Change new employee infomation
    store.Name                = Name
    store.BusinessType        = BusinessType
    store.Specialty           = Specialty
    store.AnnualSales         = AnnualSales
    store.AnnualRevenue       = AnnualRevenue
    store.YearOpened          = YearOpened
    store.SquareFeet          = SquareFeet
    store.NumberOfEmployees   = NumberOfEmployees
    store.City                = City
    store.AddressLine1        = AddressLine1
    store.AddressLine2        = AddressLine2
    store.CountryRegionName   = CountryRegionName
    
    # Save employee information
    store.save()

def CreateNewCustomerStore(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerStore = ast.literal_eval(dict)
    
    # Get special offer info from dict
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
    
    # Create new special offer object
    store = CustomerStore(Name=Name, BusinessType=BusinessType, Specialty=Specialty, AnnualSales=AnnualSales, AnnualRevenue=AnnualRevenue, YearOpened=YearOpened, SquareFeet=SquareFeet, NumberOfEmployees=NumberOfEmployees, City=City, AddressLine1=AddressLine1, AddressLine2=AddressLine2, CountryRegionName=CountryRegionName)
        
    # Save new special offer object
    store.save()

def DeleteCustomerStoreWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerStore = ast.literal_eval(dict)
    
    # Get special offer id from dict
    StoreID   = customerStore['StoreID']
    
    # Get special offer object
    store     = CustomerStore.objects.get(id=StoreID)
    
    # Delete special offer object
    store.delete()
# 
# 
# 
# 
# 
# 
#    
def GetAllCustomerIndividual():
    return CustomerIndividual.objects.all()

def SaveNewCustomerIndividual(request):
    # Converting request.body to dictionary type
    dict        = request.body.decode("UTF-8")
    customerIndividual = ast.literal_eval(dict)
    
    # Extract new information from request
    IndividualID            = customerIndividual['IndividualID']
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
    
    #Get product
    individual = CustomerIndividual.objects.get(id=IndividualID)
    
    
    # Change new employee infomation
    individual.FirstName                = FirstName
    individual.LastName        = LastName
    individual.MiddleName           = MiddleName
    individual.Title         = Title
    individual.EmailAddress       = EmailAddress
    individual.PhoneNumber          = PhoneNumber
    individual.City                = City
    individual.AddressLine1        = AddressLine1
    individual.AddressLine2        = AddressLine2
    individual.CountryRegionName   = CountryRegionName
    
    # Save employee information
    individual.save()

def CreateNewCustomerIndividual(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerIndividual = ast.literal_eval(dict)
    
    # Get special offer info from dict
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
    
    # Create new special offer object
    individual = CustomerIndividual(FirstName=FirstName, LastName=LastName, MiddleName=MiddleName, Title=Title, EmailAddress=EmailAddress, PhoneNumber=PhoneNumber, City=City, AddressLine1=AddressLine1, AddressLine2=AddressLine2, CountryRegionName=CountryRegionName)
        
    # Save new special offer object
    individual.save()

def DeleteCustomerIndividualWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    customerIndividual = ast.literal_eval(dict)
    
    # Get special offer id from dict
    IndividualID   = customerIndividual['IndividualID']
    
    # Get special offer object
    individual     = CustomerIndividual.objects.get(id=IndividualID)
    
    # Delete special offer object
    individual.delete()
    
