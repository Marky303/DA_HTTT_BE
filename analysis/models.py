import os
from dotenv import load_dotenv
load_dotenv()
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

# Get common database properties
shortLength     = 50  # os.getenv('DATABASE_SHORT_FIELD_LENGTH')
mediumLength    = 255 # os.getenv('DATABASE_MEDIUM_FIELD_LENGTH')
longLength      = 400 # os.getenv('DATABASE_LONG_FIELD_LENGTH')
decimalMaxDigit = 20  # os.getenv('DATABASE_DECIMAL_MAX_DIGIT')
decimalPlace    = 4   # os.getenv('DATABASE_DECIMAL_PLACE')

# DIMENSIONS______________________________________________________________________
class EmployeeDim(models.Model):
    # Normal fields
    Name                = models.CharField(max_length=mediumLength, blank=False) 
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + ". " + self.Name


class TerritoryDim(models.Model):
    # Normal fields
    Name                = models.CharField(max_length=shortLength, blank=False)         
    Group               = models.CharField(max_length=shortLength, blank=False)
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + ". " + self.Name
    

class CustomerDim(models.Model):
    # Normal fields
    IndividualName      = models.CharField(max_length=mediumLength, blank=True, null=True) 
    StoreName           = models.CharField(max_length=mediumLength, blank=True, null=True) 
    
    # Foreign keys
    Territory           = models.ForeignKey(TerritoryDim, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.id)


class ProductDim(models.Model):
    # Normal fields
    Name            = models.CharField(max_length=shortLength, blank=False, null=False)
    StandardCost    = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, default=0)
    ListPrice       = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, default=0)
    
    # Admin page default function
    def __str__(self):
        return str(self.id)
    
    
class SpecialOfferDim(models.Model):
    # Normal fields 
    DiscountPct     = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + " | " + str(self.DiscountPct) + "%" + " off"


# FACTS___________________________________________________________________________
class SalesOrderHeaderFact(models.Model):
    # Normal fields
    OrderDate       = models.DateTimeField()
    SubTotal        = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    TaxAmt          = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    Freight         = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    TotalDue        = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    
    # Foreign keys
    Employee        = models.ForeignKey(EmployeeDim, on_delete=models.SET_NULL, null=True)
    Customer        = models.ForeignKey(CustomerDim, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + ". " + str(self.TotalDue)
    
class SalesOrderDetailFact(models.Model):
    # Normal fields
    OrderQty                = models.PositiveIntegerField(null=False, default=1)
    LineTotal               = models.DecimalField(max_digits=decimalMaxDigit, decimal_places=decimalPlace, null=False, default=0)
    
    # Foreign keys
    Product             = models.ForeignKey(EmployeeDim, on_delete=models.SET_NULL, null=True)
    SpecialOffer        = models.ForeignKey(CustomerDim, on_delete=models.SET_NULL, null=True)
    SalesOrder          = models.ForeignKey(SalesOrderHeaderFact, on_delete=models.CASCADE, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + ". " + str(self.TotalDue)
