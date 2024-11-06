from rest_framework.serializers import ModelSerializer       
from sales.models import *

# Normal serializers___________________________________________________
# Special offer serializer
class SpecialOfferSerializer(ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = '__all__'
        
# Special offer - product serializer
class SpecialOfferProductSerializer(ModelSerializer):
    SpecialOffer = SpecialOfferSerializer()
    
    class Meta:
        model = SpecialOfferProduct
        fields = ("id", "SpecialOffer")
        
# Territory serializer
class TerritorySerializer(ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'

# Product serializer
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
        fields = ("id", "Employee", "Territory", "CustomerStore", "CustomerIndividual")
