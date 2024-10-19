import ast

# Import models
from sales.models import *

def GetAllProduct():
    return Product.objects.all()

def SaveNewProduct(request):
    # Converting request.body to dictionary type
    dict        = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Extract new information from request
    ProductID           = productInfo['ProductID']
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
    product = Product.objects.get(id=ProductID)
    
    
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

def DeleteProductWithID(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    productInfo = ast.literal_eval(dict)
    
    # Get special offer id from dict
    ProductID   = productInfo['ProductID']
    
    # Get special offer object
    product     = Product.objects.get(id=ProductID)
    
    # Delete special offer object
    product.delete()
#
#
#
#
#
#    
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
    
