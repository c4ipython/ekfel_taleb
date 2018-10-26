from django.urls import path
from accounts import views

urlpatterns = [
    path('signup_sponsor/', views.signup_sponsor, name='sign_sponsor'),
    path('login/', views.logins, name='login'),
    path('signup_student/', views.signup_student, name='sign_student'),
    path('logout/', views.logouts, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('students/', views.students, name='students'),
    path('sponsor/', views.sponsors, name='sponsors'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('delete_app/<int:idd>', views.delAppStudent, name='delete_app'),
    path('delete_appSpon/<int:idd>', views.delAppSponsor, name='delete_appS'),
    path('add_app/<str:usernamee>', views.add_app, name='add_app'),
    path('add_app_sponsor/<str:usernamee>', views.add_appSponsor, name='add_appS'),
    path('student_request/<str:usernames>', views.stuReq, name='stuReq'),
    path('sponsor_request/<str:usernames>', views.sponsor_stuReq, name='sponsor_request'),
    path('student_info/<int:id>', views.info, name='info'),
    path('sponsor_info/<int:id>', views.sponsor_info, name='sponsor_info'),
    path('ac_req/<int:id>', views.ac_req, name='ac_req'),
    path('del_req/<int:id>', views.del_req, name='del_req'),
    path('del_sponsoer/<int:id>', views.del_sponsor, name='del_sponsoer'),
    path('ac_sponsoer/<int:id>', views.ac_sponsor, name='ac_sponsoer'),
    path('del_req_sponr/<int:id>', views.del_req_spon, name='del_req_spon'),
    path('del_spon/<int:id>', views.del_sponsor_req, name='del_spon'),

]
