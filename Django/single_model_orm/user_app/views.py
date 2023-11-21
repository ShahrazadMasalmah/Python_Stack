from django.shortcuts import render, redirect
from .models import User

def show_table(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, "index.html", context)

def create_user(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    emailAddress = request.POST['email_address']
    age = request.POST['age']
    User.objects.create(first_name=firstName, last_name=lastName, email_address=emailAddress, age=age)
    return redirect("/")


