
from django.urls import path
from Students import views
urlpatterns=[
         path('Index/',views.index,name='Ind'),
path('add_re/',views.add_req,name='add_req'),






]
