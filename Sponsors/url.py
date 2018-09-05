from django.urls import path
from Sponsors import views



urlpatterns = [

path('6alab/<int:id>', views.sponserRequest, name='6alab'),


]
