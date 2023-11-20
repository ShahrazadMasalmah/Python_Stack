from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_gold),
    path('process_money', views.process_gold),
    path('destroy', views.destroy),
]