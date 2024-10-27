from django.contrib import admin


from models import *
# Register your models here.
admin.site.register(EmployeeDim)
admin.site.register(TerritoryDim)
admin.site.register(CustomerDim)
admin.site.register(ProductDim)
admin.site.register(SpecialOfferDim)
admin.site.register(SalesOrderHeaderFact)
admin.site.register(SalesOrderDetailFact)

