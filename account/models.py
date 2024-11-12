from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# ETL
from analysis.api.Functions.CRUD import *

# Manager class for user account with customized create user function
class EmployeeManager(BaseUserManager):
    # Function to create new user
    # By default django will not allow no password
    def create_user(self, email, name, password=None):
        # Raise error if there is no email
        if not email:
            raise ValueError('User must have an email address')
        
        # Normalizer normalizing email (lowercasing,...) 
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        # Hashing password for security reasons
        user.set_password(password)
        
        # Finally save the user
        user.save()
        
        # ETL
        CreateEmployeeDimETL(user)
        
        return user

# Custom user model goes here.
class Employee(AbstractBaseUser, PermissionsMixin):
    # Important user fields
    email               = models.EmailField(max_length=255, unique=True)
    name                = models.CharField(max_length=255)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    
    # Other informative user fields
    JobTitle            = models.CharField(max_length=50, default='Employee')
    PhoneNumber         = models.CharField(max_length=20, blank=True)
    City                = models.CharField(max_length=20, null=True, blank=True)
    AddressLine1        = models.CharField(max_length=20, null=True, blank=True)
    AddressLine2        = models.CharField(max_length=20, null=True, blank=True)
    CountryRegionName   = models.CharField(max_length=20, null=True, blank=True)
    
    # If UserAccount/Employee is a manager
    isManager           = models.BooleanField(default=False)
    
    # If UserAccount is an employee
    isEmployee          = models.BooleanField(default=True)
    
    # Choosing email as username for login/signup
    USERNAME_FIELD      = 'email'
    
    # Required fields, must not be null
    REQUIRED_FIELDS     = ['name']
    
    objects             = EmployeeManager()
    
    # Functions to get user information
    def get_full_name(self):
        return self.name
    
    # Admin page default function
    def __str__(self):
        return self.name 
