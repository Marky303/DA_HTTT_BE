from rest_framework.serializers import ModelSerializer       

from sales.models import *

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
