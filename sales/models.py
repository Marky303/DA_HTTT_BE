import os
from dotenv import load_dotenv
load_dotenv()
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

# Import foreign key models
from account.models import Employee

# Regex
phone_number_validator = RegexValidator(
    regex=r'^[\d\+\-\(\)\s]+$',
    message='Phone number can only contain digits, spaces, and the following symbols: + - ( )'
)

# Get common database properties
shortLength     = 50  # os.getenv('DATABASE_SHORT_FIELD_LENGTH')
mediumLength    = 255 # os.getenv('DATABASE_MEDIUM_FIELD_LENGTH')
longLength      = 400 # os.getenv('DATABASE_LONG_FIELD_LENGTH')
decimalMaxDigit = 20  # os.getenv('DATABASE_DECIMAL_MAX_DIGIT')
decimalPlace    = 4   # os.getenv('DATABASE_DECIMAL_PLACE')

# Create your models here.
class SpecialOffer(models.Model):
    # Primary key
    # SpecialOfferID = models.IntegerField(primary_key=True)
    
    # Normal fields
    Description     = models.CharField(max_length=mediumLength, blank=False, null=False)         
    Type            = models.CharField(max_length=shortLength, blank=False, null=False)  
    
    StartDate       = models.DateTimeField(null=False)
    EndDate         = models.DateTimeField(null=False)
    
    MinQty          = models.PositiveIntegerField(default=0)
    MaxQty          = models.PositiveIntegerField(null=True)
    
    DiscountPct     = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, validators=[MinValueValidator(0), MaxValueValidator(1)])



class Product(models.Model):
    # Primary key
    # ProductID       = models.IntegerField(primary_key=True)
    
    # Normal fields
    Name            = models.CharField(max_length=shortLength, blank=False, null=False)
    Manufacturer    = models.CharField(max_length=mediumLength, blank=True, null=True)
    Summary         = models.CharField(max_length=mediumLength, blank=True, null=True)
    WarrantyPeriod  = models.CharField(max_length=shortLength, blank=True, null=True)
    RiderExperience = models.CharField(max_length=mediumLength, blank=True, null=True)
    Description     = models.CharField(max_length=longLength, blank=True, null=True)
    Size            = models.CharField(max_length=shortLength, blank=False, null=False)
    Style           = models.CharField(max_length=shortLength, blank=False, null=False)
    
    StandardCost    = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, default=0)
    ListPrice       = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, default=0)
    
    
    
class SpecialOfferProduct(models.Model):
    # Foreign keys
    SpecialOffer    = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE, null=False)
    Product         = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    # Admin page default function
    def __str__(self):
        return "Special Offer and Product: " + str(self.SpecialOffer) + " + " + str(self.Product)



class Territory(models.Model):
    # Primary key
    # TerritoryID         = models.IntegerField(primary_key=True)
    
    # Normal fields
    Name                = models.CharField(max_length=shortLength, blank=False)         
    Group               = models.CharField(max_length=shortLength, blank=False)
    SalesYTD            = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    SalesLastYear       = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    
    # Admin page default function
    def __str__(self):
        return self.TerritoryID + ". " + self.Name



class CustomerStore(models.Model):
    # Primary key
    # StoreID             = models.IntegerField(primary_key=True)
    
    # Normal fields
    Name                = models.CharField(max_length=shortLength, blank=False, null=False)         
    BusinessType        = models.CharField(max_length=shortLength, blank=False, null=True)
    Specialty           = models.CharField(max_length=shortLength, blank=False, null=True)
    
    AnnualSales         = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=True)
    AnnualRevenue       = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=True)
    
    YearOpened          = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    SquareFeet          = models.PositiveIntegerField(null=True)
    NumberOfEmployees   = models.PositiveIntegerField(null=True)
    
    City                = models.CharField(max_length=decimalMaxDigit, null=True, blank=True)
    AddressLine1        = models.CharField(max_length=decimalMaxDigit, null=True, blank=True)
    AddressLine2        = models.CharField(max_length=decimalMaxDigit, null=True, blank=True)
    CountryRegionName   = models.CharField(max_length=decimalMaxDigit, null=True, blank=True)
    
    # Admin page default function
    def __str__(self):
        return self.Name + ": " + self.BusinessType
    
    
class CustomerIndividual(models.Model):
    # Primary key
    # IndividualID        = models.IntegerField(primary_key=True)

    # Normal fields
    FirstName           = models.CharField(max_length=decimalMaxDigit, blank=False, null=False)
    LastName            = models.CharField(max_length=decimalMaxDigit, blank=False, null=False)
    MiddleName          = models.CharField(max_length=decimalMaxDigit, blank=False, null=True)
    
    Title               = models.CharField(max_length=shortLength, blank=False)         
    EmailAdress         = models.CharField(max_length=mediumLength, blank=False)  
    PhoneNumber         = models.CharField(max_length=decimalMaxDigit, validators=[phone_number_validator], blank=False)
    
    City                = models.CharField(max_length=shortLength, null=True, blank=True)
    AddressLine1        = models.CharField(max_length=mediumLength, null=True, blank=True)
    AddressLine2        = models.CharField(max_length=mediumLength, null=True, blank=True)
    CountryRegionName   = models.CharField(max_length=shortLength, null=True, blank=True)
    
    # Admin page default function
    def __str__(self):
        return self.FirstName + " " + self.LastName + " / " + self.EmailAdress
    
    
class Customer(models.Model):
    # Primary key
    # CustomerID              = models.IntegerField(primary_key=True)
    
    # Foreign keys
    Employee                = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    Territory               = models.ForeignKey(Territory, on_delete=models.SET_NULL, null=True)
    CustomerStore           = models.ForeignKey(CustomerStore, on_delete=models.SET_NULL, null=True)
    CustomerIndividual      = models.ForeignKey(CustomerIndividual, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.CustomerID)
    


class SalesOrderHeader(models.Model):
    # Primary key
    # SalesOrderID    = models.IntegerField(primary_key=True)
    
    # Normal fields
    OrderDate       = models.DateTimeField()
    DueDate         = models.DateTimeField()
    ShipDate        = models.DateTimeField()
    
    ShipMethod      = models.CharField(max_length=shortLength, blank=True, null=True)
    Comment         = models.CharField(max_length=mediumLength, default='None')
    
    SubTotal        = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    TaxAmt          = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    Freight         = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    TotalDue        = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    
    # Foreign keys
    Employee                = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    Customer                = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Territory               = models.ForeignKey(Territory, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return "Order " + str(self.id) + ": " + str(self.SubTotal)



class SalesOrderDetail(models.Model):
    # Primary key
    # SalesOrderDetailID      = models.IntegerField(primary_key=True)
    
    # Normal fields
    CarrierTrackingNumber   = models.CharField(max_length=shortLength, blank=True, null=True)
    
    OrderQty                = models.PositiveIntegerField(null=False, default=1)
    UnitPrice               = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    UnitPriceDiscount       = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    LineTotal               = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    
    # Foreign keys
    SalesOrder              = models.ForeignKey(SalesOrderHeader, on_delete=models.CASCADE, null=False)
    Product                 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    SpecialOffer            = models.ForeignKey(SpecialOffer, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return "Order " + str(self.SalesOrderDetailID) + ": " + str(self.LineTotal)