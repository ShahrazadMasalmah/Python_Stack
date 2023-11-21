from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")

def destroy(request, number):
    return redirect("/blogs")

