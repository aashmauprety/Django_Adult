from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'adultcontent-home'),
    path('check', views.check, name = 'check'),
]
