from django.shortcuts import render
from django.contrib.auth.models import User, Group 
from .forms import UserForm
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



def newUser(request):
     form=UserForm
     if request.method=='POST':
          form=UserForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
              
               g = Group.objects.get(name='Customer')
               u = User.objects.latest('id')

               g.user_set.add(u)

               form=UserForm()
     else:
          form=UserForm()
     return render(request, 'serviceapp/userform.html', {'form': form})


