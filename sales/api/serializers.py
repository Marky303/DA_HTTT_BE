from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer       
from rest_framework import serializers

from sales.models import *


class ProductInfoSerializer(ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'
        
class CustomerStoreInfoSerializer(ModelSerializer):
    class Meta:
        model = CustomerStore
        fields = '__all__'
        
class CustomerIndividualInfoSerializer(ModelSerializer):
    class Meta:
        model = CustomerIndividual
        fields = '__all__'
        
        
        
# EXAMPLE SERIALIZER FOR TESTING
# Note model for testing
# from sales.models import Note
# from rest_framework.serializers import ModelSerializer        

# # Note serializer
# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'