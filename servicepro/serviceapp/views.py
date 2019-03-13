from django.shortcuts import render
from django.contrib.auth.models import User, Group 
from .forms import UserForm, VehicleForm
from .models import CarService, Vehicle, Appointment, AppointmentDetail
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'serviceapp/index.html')

def loginmessage(request):
    return render(request, 'loginmessage.html')

def logoutmessage(request):
    return render(request, 'logoutmessage.html')

def carservices(request):
     serv_list=CarService.objects.all()
     return render(request, 'serviceapp/carservices.html', {'serv_list': serv_list})

@login_required
def vehicles(request):
     u=request.user.id
     v_list=Vehicle.objects.filter(owner=u)
     return render (request, 'serviceapp/vehicles.html', {'v_list': v_list})

#Forms

def newUser(request):
     form=UserForm
     if request.method=='POST':
          form=UserForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               #retreive the customer group
               g = Group.objects.get(name='Customer')
               #get the user id of the user just created
               u = User.objects.latest('id')
               #add the user to the customer group
               g.user_set.add(u)

               form=UserForm()
     else:
          form=UserForm()
     return render(request, 'serviceapp/vehicleform.html', {'form': form})

def addVehicle(request):
     form=VehicleForm
     if request.method=='POST':
          form=VehicleForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
              
               g = Group.objects.get(name='Customer')
               form=UserForm()
     else:
          form=VehicleForm()
     return render(request, 'serviceapp/userform.html', {'form': form})

def NewAppointment(request):
     form=AppointmentForm
     if request.method=='POST':
          form=AppointmentForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
              
               g = Group.objects.get(name='Customer')
               form=AppointmentForm()
     else:
          form=AppointmentForm()
     return render(request, 'serviceapp/appointmentform.html', {'form': form})

     


