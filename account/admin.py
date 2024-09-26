from django.contrib import admin
from .models import *

# Register account models
admin.site.register(UserAccount)
admin.site.register(Note)