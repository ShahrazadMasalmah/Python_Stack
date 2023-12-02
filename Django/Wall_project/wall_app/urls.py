from django.urls import path
from . import views


urlpatterns = [
    path('wall', views.index),
    path('add-message', views.addMessage),
    path('add-comment', views.addComment),
    path('delete-message', views.deleteMessage),
    path('logout', views.logout)
]
