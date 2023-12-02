from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def registerLogin(request):
    return render(request, "register_login.html")

def userRegister(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        hash_password =  bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = firstName, last_name = lastName, email = email, password = hash_password)
        request.session['user_id'] = new_user.id
        return redirect("/books")

def userLogin(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        this_user = User.objects.filter(email = request.POST['email'])
        request.session['user_id'] = this_user[0].id  
        return redirect("/books")  

def addBook(request):
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "this_user" : this_user[0],
        "books" : Book.objects.all(),
        "users" : User.objects.all()
    } 
    return render(request, "add_book.html", context)

def check_and_addBook(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books") 
    else:
        this_user = User.objects.get(id = request.session['user_id'])
        title = request.POST['title']
        description = request.POST['description']
        new_book = Book.objects.create(title = title, desc = description, uploaded_by = this_user)
        new_book.users_liked.add(this_user)
        request.session['book_id'] = new_book.id 
        return redirect("/books")

def logout(request):
    request.session.flush()
    return redirect("/")

def editBook(request, id):
    this_book = Book.objects.get(id=id)
    this_user = User.objects.filter(id = request.session['user_id'])
    book_likers = this_book.users_liked.all()
    context = {
        "this_user" : this_user[0], 
        "book_likers": book_likers,
        "this_book" : this_book
    }
    return render(request, "edit_book.html", context)

def UpdateBook(request, id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/books/{id}/edit") 
    else:
        this_book = Book.objects.get(id=id)
        this_book.title = request.POST['title']
        this_book.desc = request.POST['description']
        this_book.save()
        return redirect("/books")
    
def deleteBook(request, id):
    this_book = Book.objects.get(id=id)
    this_book.delete()
    return redirect("/books")    

def ShowBook(request, id):
    this_user = User.objects.filter(id = request.session['user_id'])
    this_book = Book.objects.get(id=id) 
    book_likers = this_book.users_liked.all()
    context = {
        "this_user" : this_user[0],
        "this_book" : this_book,
        "book_likers" : book_likers,
    }
    return render(request, "show_book.html", context)

def FavoriteTheBook(request, id):
    this_user = User.objects.filter(id = request.session['user_id'])
    this_book = Book.objects.get(id=id)
    this_book.users_liked.add(this_user[0])
    return redirect("/books")

def unfavoriteTheBook(request, id):
    this_user = User.objects.filter(id = request.session['user_id'])
    this_book = Book.objects.get(id=id)
    this_book.users_liked.remove(this_user[0])
    return redirect("/books")

def userViewBook(request):
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "this_user" : this_user[0]
    }
    return render(request, "user_viewBook.html", context)