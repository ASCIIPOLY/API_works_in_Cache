from django.contrib import admin
from .models import vehicle_model,vehicle
# Register your models here.


admin.site.register(vehicle)
admin.site.register(vehicle_model)