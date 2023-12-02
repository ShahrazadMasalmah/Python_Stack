from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import *
import bcrypt

def showPage(request):
    return render(request, "index.html")

def registerUser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")  
    else:
        register = request.POST['submit']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        birthday = request.POST['birthday']
        password = request.POST['password']
        hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this_User = User.objects.create(first_name = firstName, last_name = lastName, 
                                        email = email, birthday = birthday, password = hash_password) 
        request.session['user_id'] = this_User.id
        request.session['submit'] = register
        return redirect("/wall")
    

def validate_login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/") 
    else: 
        login = request.POST['submit']
        user = User.objects.get(email = request.POST['email'])
        password = request.POST['password']
        if bcrypt.checkpw(password.encode(), user.password.encode()): 
            request.session['user_id'] = user.id
            request.session['submit'] = login
            return redirect("/wall")
        else:
            messages.error(request ,"The password is inccorect!")
            return redirect("/")

