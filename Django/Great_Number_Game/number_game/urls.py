from django.urls import path
from . import views

urlpatterns = [
    path('', views.safe_number),
    path('guess', views.compare),
    path('try', views.try_again),
    path('result', views.show_result),
]