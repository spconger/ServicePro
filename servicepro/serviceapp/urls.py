from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('newuser/', views.newUser, name='newuser'),
    path('carservices/', views.carservices, name='carservices'),
    path('vehicles/', views.vehicles, name='vehicles')
]