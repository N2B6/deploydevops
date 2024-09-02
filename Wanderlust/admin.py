"""
Module containing model admin registrations for the Wanderlust application.
"""

from django.contrib import admin  # Only import necessary module
from .models import WanderlustUser, Trip
# Register your models here.


admin.site.register(WanderlustUser)
admin.site.register(Trip)
