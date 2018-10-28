
from django.urls import path

from home import views

urlpatterns = [
    path ('',views.home,name='home'),
    path ('contact/',views.contact,name='contact'),
    path ('about/',views.about,name='about'),
    path ('c4i/', views.c4i, name='c4i'),
    path ('devteam/',views.devteam,name='devteam'),
    path ('dashboard',views.dashboard,name='dashboard')

]
