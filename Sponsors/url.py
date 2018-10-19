from django.urls import path
from Sponsors import views



urlpatterns = [

path('kafalat/req/<int:id>', views.sponserRequest, name='6alab'),
path('kafalat/', views.displayKafalat, name='kafalat'),
path('kafalaty/', views.displayMyKafalat, name='kafalaty'),
path('kafalaty/del/<int:id>', views.sponserdelete, name='delete'),
path('admin/req/<int:id>', views.reqAdmin, name='reqAdmin'),
path('admin/del/<int:id>', views.delAdmin, name='delAdmin'),

]
