from django.shortcuts import render, redirect
from .models import Book, Author

def showBooks(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request, "createBook.html", context)

def createBook(request):
    title = request.POST['title']
    description =  request.POST['description'] 
    Book.objects.create(title = title, desc = description)
    return  redirect("/")

def viewBook(request, id):
    this_book = Book.objects.get(id=id)
    context = {
        "book": this_book,
        "non_assoc_authors" : Author.objects.exclude(books=this_book)
    }
    return render(request, "viewBook.html", context)

def addAuthorToBook(request):
    book_id = request.POST['book']
    this_book = Book.objects.get(id=book_id)
    author_id = request.POST['author']
    this_author = Author.objects.get(id=author_id)
    this_book.authors.add(this_author)
    return redirect(f"/books/{book_id}")

def showAuthors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, "createAuthor.html", context) 

def createAuthor(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    notes =  request.POST['notes'] 
    Author.objects.create(first_name = firstName, last_name = lastName, notes = notes)
    return  redirect("/authors")

def viewAuthor(request, id):
    this_author = Author.objects.get(id=id)
    context = {
        "author": this_author,
        "non_assoc_books" : Book.objects.exclude(authors=this_author)
    }
    return render(request, "viewAuthor.html", context) 

def addBookToAuthor(request):
    author_id = request.POST['author']
    this_author = Author.objects.get(id=author_id)
    book_id = request.POST['book']
    this_book = Book.objects.get(id=book_id)
    this_author.books.add(this_book)
    return redirect(f"/authors/{author_id}")       

