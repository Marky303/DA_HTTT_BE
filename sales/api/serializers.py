from rest_framework.serializers import ModelSerializer       
from sales.models import *
from rest_framework import serializers

# Normal serializers___________________________________________________
# Special offer serializer
class SpecialOfferSerializer(ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = '__all__'
        
# Special offer - product serializer
class SpecialOfferProductSerializer(ModelSerializer):
    class Meta:
        model = SpecialOfferProduct
        fields = '__all__'
        
# Territory serializer
class TerritorySerializer(ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'

class ProductSerializer(ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
# Sales order related serializer_______________________________________
# Sales order detail serializer
class SalesOrderDetailSerializer(ModelSerializer):
    # Nested serializer
    Product = ProductSerializer(many=False)
    
    class Meta:
        model = SalesOrderDetail
        fields = '__all__'

# Sales order header serializer
class SalesOrderHeaderSerializer(ModelSerializer):
    # Nested serializer
    SalesOrderDetail = SalesOrderDetailSerializer(many=True)
    
    class Meta:
        model = SalesOrderHeader
        fields = '__all__'



# Customer related serializer__________________________________________
class CustomerStoreInfoSerializer(ModelSerializer):
    class Meta:
        model = CustomerStore
        fields = '__all__'
        
class CustomerIndividualInfoSerializer(ModelSerializer):
    class Meta:
        model = CustomerIndividual
        fields = '__all__'
        
class CustomerInfoSerializer(ModelSerializer):
    CustomerStore = CustomerStoreInfoSerializer()
    CustomerIndividual = CustomerIndividualInfoSerializer()
    
    class Meta:
        model = Customer
        fields = ("Employee", "Territory", "CustomerStore", "CustomerIndividual")
        
# EXAMPLE SERIALIZER FOR TESTING
# Note model for testing
# from sales.models import Note
# from rest_framework.serializers import ModelSerializer        

# # Note serializer
# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'
