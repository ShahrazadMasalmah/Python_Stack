from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_table),
    path('add_user', views.create_user),
]