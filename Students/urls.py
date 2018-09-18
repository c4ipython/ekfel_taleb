
from django.urls import path
from Students import views
urlpatterns=[
         path('Index/',views.index,name='Ind'),
path('add_re/',views.add_req,name='add_req'),
path('view_rq/',views.view_req,name='view_rq'),
path('view_rq/<int:id>',views.accept_req,name='view_rq'),
path('view_rq/<int:id>',views.disable_req,name='view_rq'),
path('view_rq/edit/<int:id>',views.edit_req,name='edit_re'),







]
