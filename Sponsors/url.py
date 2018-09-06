from django.urls import path
from Sponsors import views



urlpatterns = [

path('6alab/<int:id>', views.sponserRequest, name='6alab'),
path('delete/<int:id>',views.sponserdelete, name='delete'),
path('kafalat/', views.displayKafalat, name='kafalat'),
path('kafalaty/', views.displayMyKafalat, name='kafalaty'),


]
