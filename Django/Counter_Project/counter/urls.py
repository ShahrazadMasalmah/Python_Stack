from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter),
    path('destroy_session', views.destroy_session),
    path('count', views.reset_add),
]