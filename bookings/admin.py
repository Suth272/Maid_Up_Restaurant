from django.contrib import admin
from .models import Table, Reservation

admin.site.register(Table)  # Register Table model for admin
admin.site.register(Reservation)  # Register Reservation model for admin
