from django.urls import path
from accounts import views

urlpatterns = [
    path('signup_sponsor/', views.signup_sponsor, name='sign_sponsor'),
    path('login/', views.logins, name='login'),
    path('signup_student/', views.signup_student, name='sign_student'),
    path('logout/', views.logouts, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('students/', views.students, name='students'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('delete_app/<int:idd>', views.delAppStudent, name='delete_app'),
    path('add_app/<str:usernamee>', views.add_app, name='add_app'),
    path('student_request/<str:usernames>', views.stuReq, name='stuReq'),
    path('student_info/<int:id>', views.info, name='info'),

]
