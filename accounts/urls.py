from django.urls import path
from accounts import views

urlpatterns = [
    path('signUp/', views.signup_sponsor, name='sign_sponsor'),
    path('login/', views.logins, name='sign_sponsor'),
]
