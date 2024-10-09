from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerIndividual)
admin.site.register(CustomerStore)
admin.site.register(Territory)
admin.site.register(SalesOrderHeader)
