from django.contrib import admin

from .models import Note, UserAccount

# Register your models here.

# User model
admin.site.register(UserAccount)

# Registering models in order to be edited in admin site
admin.site.register(Note)