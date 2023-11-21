from django.shortcuts import render, HttpResponse

def display(request):
    return HttpResponse("Placeholder to display all the surveys created")

def display_new(request):
    return HttpResponse("Placeholder for users to add a new survey")    
