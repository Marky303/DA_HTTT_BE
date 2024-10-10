from rest_framework.serializers import ModelSerializer       
from rest_framework import serializers

from sales.models import *

# Special offer serializer
class SpecialOfferSerializer(ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = '__all__'