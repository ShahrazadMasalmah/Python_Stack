from django.urls import path
from . import views
urlpatterns = [
   path('', views.display),
   path('new', views.display_new),
]