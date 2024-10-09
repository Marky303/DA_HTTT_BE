from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer       
from rest_framework import serializers

# Import models for serializing
from account.models import *

# Get custom user model
from django.contrib.auth import get_user_model
User = get_user_model()

# Serializer for user creation
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password') 
                
                
# Serializer for getting employee information
class UserinfoSerializer(ModelSerializer):    
    class Meta:
        model = Employee
        fields = ('email', 'name', 'JobTitle', 'PhoneNumber', 'City', 'AddressLine1', 'AddressLine2', 'CountryRegionName', 'isManager')
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

# EXAMPLE SERIALIZER FOR TESTING
# Note model for testing
from account.models import Note
from rest_framework.serializers import ModelSerializer        

# Note serializer
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'