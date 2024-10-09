from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

# Import foreign key models
from account.models import UserAccount

# Regex
phone_number_validator = RegexValidator(
    regex=r'^[\d\+\-\(\)\s]+$',
    message='Phone number can only contain digits, spaces, and the following symbols: + - ( )'
)

# Create your models here.
class Territory(models.Model):
    # Basic Territory info
    Name = models.CharField(max_length=20, blank=False)         
    Group = models.CharField(max_length=50, blank=False)
    
    # Statistical info... TODO
    SalesYTD = models.DecimalField(max_digits=20, decimal_places=4, null=False, default=0)
    SalesLastYear = models.DecimalField(max_digits=20, decimal_places=4, null=False, default=0)
    
    # Admin page default function
    def __str__(self):
        return self.Name + " region"


class CustomerStore(models.Model):
    # Mandantory store info
    Name = models.CharField(max_length=30, blank=False)         
    BusinessType = models.CharField(max_length=20, blank=False)
    Specialty = models.CharField(max_length=20, blank=False)
    
    # Additional store info
    AnnualSales = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    AnnualRevenue = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    YearOpened = models.PositiveIntegerField(
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    SquareFeet = models.PositiveIntegerField(null=True)
    NumberOfEmployees = models.PositiveIntegerField(null=True)
    
    # Address info
    City = models.CharField(max_length=20, default='Nowhere')
    AddressLine1 = models.CharField(max_length=20, default='Nowhere')
    AddressLine2 = models.CharField(max_length=20, default='Nowhere')
    CountryRegionName = models.CharField(max_length=20, default='Nowhere')
    
    # Admin page default function
    def __str__(self):
        return self.Name + ": " + self.BusinessType
    
    
class CustomerIndividual(models.Model):
    # Mandantory individual info
    Title = models.CharField(max_length=30, blank=False)         
    EmailAdress = models.EmailField(max_length=255, blank=False)
    PhoneNumber = models.CharField(max_length=20, validators=[phone_number_validator], blank=False)
    FirstName = models.CharField(max_length=20, blank=False)
    LastName = models.CharField(max_length=20, blank=False)
    
    # Additional individual info
    MiddleName = models.CharField(max_length=20, blank=True)
    Age = models.PositiveIntegerField(null=True)
    
    # Address info
    City = models.CharField(max_length=20, default='Nowhere')
    AddressLine1 = models.CharField(max_length=20, default='Nowhere')
    AddressLine2 = models.CharField(max_length=20, default='Nowhere')
    CountryRegionName = models.CharField(max_length=20, default='Nowhere')
    
    # Admin page default function
    def __str__(self):
        return self.FirstName + " " + self.LastName + " / " + self.EmailAdress
    
    
class Customer(models.Model):
    # Foreign keys
    EmployeeID = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
    TerritoryID = models.ForeignKey(Territory, on_delete=models.SET_NULL, blank=True, null=True)
    CustomerStoreID = models.ForeignKey(CustomerStore, on_delete=models.SET_NULL, blank=True, null=True)
    CustomerIndividualID = models.ForeignKey(CustomerIndividual, on_delete=models.SET_NULL, blank=True, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.id)