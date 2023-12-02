from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerLogin),
    path('register', views.userRegister),
    path('login', views.userLogin),
    path('books', views.addBook),
    path('add-book', views.check_and_addBook),
    path('logout', views.logout),
    path('books/<int:id>/edit', views.editBook),
    path('update/<int:id>', views.UpdateBook),
    path('delete/<int:id>', views.deleteBook),
    path('books/<int:id>', views.ShowBook),
    path('add_to_favorite/<int:id>', views.FavoriteTheBook),
    path('unfavorite/<int:id>', views.unfavoriteTheBook),
    path('books/view', views.userViewBook)
]