from django.urls import path
from . import views

urlpatterns = [
    path('', views.showBooks),
    path('add-book', views.createBook),
    path('books/<int:id>', views.viewBook),
    path('add-author-book', views.addAuthorToBook),
    path('authors', views.showAuthors),
    path('add-author', views.createAuthor),
    path('authors/<int:id>', views.viewAuthor),
    path('add-book-author', views.addBookToAuthor),
]