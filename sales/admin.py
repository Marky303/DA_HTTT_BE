from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerIndividual)
admin.site.register(CustomerStore)
admin.site.register(Territory)
admin.site.register(SalesOrderHeader)
admin.site.register(SalesOrderDetail)
admin.site.register(SpecialOffer)
admin.site.register(SpecialOfferProduct)
admin.site.register(Product)
