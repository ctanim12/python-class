from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("",homepage,name='home'),
    path("about/",aboutpage,name='about.html'),
    path("contact/",contactpage,name='contact.html')
    
]