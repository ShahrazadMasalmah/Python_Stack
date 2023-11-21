from django.shortcuts import render, HttpResponse, redirect

def register(request):
    return HttpResponse("Placeholder for users to create a new user record")

def log_in(request):
    return HttpResponse("Placeholder for users to log in")

def goFor(request):
    return redirect("/register")

def string(request):
    return HttpResponse("Placeholder to later display all the list of users")   

def index(request):
    return redirect("/blogs")             