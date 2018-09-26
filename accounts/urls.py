from django.urls import path
from accounts import views

urlpatterns = [
    path('signup_sponsor/', views.signup_sponsor, name='sign_sponsor'),
    path('login/', views.logins, name='login'),
    path('signup_student/', views.signup_student, name='sign_student'),
    path('logout/', views.logouts, name='logout'),
    path('profile/', views.profile, name='profile'),

]
