from django.urls import path
from Sponsors import views



urlpatterns = [

path('kafalat/', views.displayKafalat, name='kafalat'),
path('kafalat/req/<int:id>', views.sponserRequest, name='kafalatRequest'),
path('kafalaty/', views.displayMyKafalat, name='kafalaty'),
path('kafalaty/del/<int:id>', views.sponserdelete, name='kafalatyDelete'),
path('kafalat/adminA/<int:id>', views.acceptAdmin, name='adminA'),
path('kafalat/adminb/<int:id>', views.refuseAdmin, name='adminb'),
path('kafalat/admind/<int:id>', views.delAdmin, name='admind'),


]
