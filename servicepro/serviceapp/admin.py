from django.contrib import admin
from .models import Vehicle, CarService, Appointment, AppointmentDetail

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(CarService)
admin.site.register(Appointment)
admin.site.register(AppointmentDetail)