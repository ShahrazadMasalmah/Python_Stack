from django.urls import path
from . import views
urlpatterns = [
    path('', views.show),
    path('add-dojo', views.createDojo),
    path('add-ninja', views.createNinja),
    path('delete', views.deleteDojoNinjas)
]