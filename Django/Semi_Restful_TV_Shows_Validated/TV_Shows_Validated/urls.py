from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.goTo),
    path('shows/new', views.adding_Tv_Show),
    path('shows/create', views.createShow),
    path('shows/<int:id>', views.showDetail),
    path('shows', views.showTable),
    path('shows/<int:id>/destroy', views.delete),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.showChange)
]    