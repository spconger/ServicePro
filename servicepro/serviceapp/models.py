from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarService(models.Model):
    servicename=models.CharField(max_length=255)
    partsprice=models.DecimalField(max_digits=10, decimal_places=2)
    laborprice=models.DecimalField(max_digits=10, decimal_places=2)
    servicedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.servicename
    
    class Meta:
        db_table='services'
        verbose_name_plural = 'carservices'

class Vehicle(models.Model):
    vehiclemake=models.CharField(max_length=255)
    vehiclemodel=models.CharField(max_length=255)
    licenseplate=models.CharField(max_length=15)
    licensestate=models.CharField(max_length=2)
    owner=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.licenseplate

    class Meta:
        db_table='vehicle'
        verbose_name_plural='vehicles'

class Appointment(models.Model):
    appointmentdate=models.DateField()
    appointmenttime=models.TimeField()
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicle) + str(self.appointmentdate)
    
    class Meta:
        db_table='appointment'
        verbose_name_plural='appointments'

class AppointmentDetail(models.Model):
    appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    carservice=models.ForeignKey(CarService, on_delete=models.CASCADE)
    completedTime=models.TimeField()
    notes=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.carservice)

    class Meta:
        db_table='appointmentdetail'
        verbose_name_plural='appointmentdetails'






        
        