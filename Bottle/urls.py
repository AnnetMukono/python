from django.conf.urls import include,url
from django.contrib import admin
from Bottle import views

urlpatterns = [
  
     url (r'^update$',views.update, name='student'),
]
