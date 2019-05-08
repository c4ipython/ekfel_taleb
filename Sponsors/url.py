from django.urls import path
from Sponsors import views



urlpatterns = [
path('adminKafalat/', views.adminDisplayKafalatListView.as_view(), name='adminKafalat'),
path('kafalat/', views.displayKafalatListView.as_view(), name='kafalat'),
path('kafalaty/', views.displayMyKafalatListView.as_view(), name='kafalaty'),
path('kafalat/req/<int:id>', views.addSponserRequest, name='kafalatRequest'),
path('kafalaty/del/<int:id>', views.sponserdelete, name='kafalatyDelete'),
path('kafalat/adminA/<int:id>', views.adminAncceptTheSponserRequest, name='adminA'),
path('kafalat/adminb/<int:id>', views.adminRefuseTheSponserRequest, name='adminb'),
path('kafalat/admind/<int:id>', views.adminDeleteTheSponser, name='admind')

]
