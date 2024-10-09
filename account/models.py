from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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
    City                = models.CharField(max_length=20, default='Nowhere')
    AddressLine1        = models.CharField(max_length=20, default='Nowhere')
    AddressLine2        = models.CharField(max_length=20, default='Nowhere')
    CountryRegionName   = models.CharField(max_length=20, default='Nowhere')
    
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

# EXAMPLE MODEL FOR TESTING
class Note(models.Model):
    # Foreign key
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    
    # Admin page default function
    def __str__(self):
        return self.body