
from django.urls import path, include
from events import views

urlpatterns = [
    path ('add/',views.add,name='add_event'),
    path ('list/',views.viewEvents,name='viewEvents'),
    path ('list/<int:id>',views.deleted,name='delteEvents'),


]
