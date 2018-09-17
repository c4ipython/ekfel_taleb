from django.urls import path
from accounts import views

urlpatterns = [
    path('signUp/', views.signup_sponsor, name='sign_sponsor'),
    path('login/', views.logins, name='login'),
    path('signUpStudent/', views.signup_student, name='sign_student'),

]
