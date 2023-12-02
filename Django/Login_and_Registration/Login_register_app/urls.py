from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPage),
    path('register', views.registerUser),
    path('success', views.successLoad),
    path('login', views.validate_login),
    path('logout', views.logout)
]