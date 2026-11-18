from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts import views

urlpatterns = [
    path('register', views.RegisterAPI.as_view()),
    path('login', obtain_auth_token),
    path('logout', views.LogoutAPI.as_view()),
]
