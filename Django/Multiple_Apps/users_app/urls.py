from django.urls import path
from . import views
app_name = "users_app"

urlpatterns = [
   path('register', views.register),
   path('login', views.log_in),
   path('users/new', views.goFor),
   path('users', views.string),
   path('', views.index)
]